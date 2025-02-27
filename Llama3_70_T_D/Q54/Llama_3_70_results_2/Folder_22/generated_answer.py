def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(nums):
    x = nums[85]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            is_right_truncatable = True
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[:-i])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)