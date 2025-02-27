def all_right_truncatable_prime(nums):
    x = nums[86]
    right_truncatable_primes = []
    for num in range(x, 0, -1):
        if is_prime(num):
            if is_right_truncatable_prime(num):
                right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    if right_truncatable_primes:
        return right_truncatable_primes
    else:
        return []

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    last_digit = num % 10
    for i in range(last_digit, 0, -1):
        num = num // 10
        if not is_prime(num):
            return False
    return True