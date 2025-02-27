def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return primes

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    if len(nums) <= 433:
        return []
    x = nums[433]
    primes = sieve_of_eratosthenes(1000000)
    single_digit_primes = {2, 3, 5, 7}
    double_digit_primes = {11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    left_right_truncatable_primes = set()
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not primes[num]:
            continue
        truncated = True
        for i in range(1, len(str_num)):
            left_truncated = int(str_num[i:])
            right_truncated = int(str_num[:-i])
            if i == len(str_num) - 1 and left_truncated not in single_digit_primes and (right_truncated not in single_digit_primes):
                continue
            elif i < len(str_num) - 1 and (left_truncated not in double_digit_primes or right_truncated not in double_digit_primes):
                truncated = False
                break
        if truncated:
            left_right_truncatable_primes.add(num)
    return sorted(list(left_right_truncatable_primes), reverse=True)