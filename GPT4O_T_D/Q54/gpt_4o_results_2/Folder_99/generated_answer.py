def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes(limit):
    rt_primes = [2, 3, 5, 7]
    truncatable_primes = []
    for prime in rt_primes:
        stack = [prime]
        while stack:
            num = stack.pop()
            if num < limit and num not in truncatable_primes:
                if is_prime(num):
                    truncatable_primes.append(num)
                    for digit in range(10):
                        new_num = num * 10 + digit
                        if is_prime(new_num):
                            stack.append(new_num)
    truncatable_primes.sort()
    return truncatable_primes

def all_right_truncatable_prime(nums):
    if len(nums) <= 758:
        return []
    x = nums[758]
    return right_truncatable_primes(x)