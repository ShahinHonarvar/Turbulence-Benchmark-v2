from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def is_truncatable_prime(x):
    if not is_prime(x):
        return False
    x_str = str(x)
    for i in range(1, len(x_str)):
        if not is_prime(int(x_str[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[70]
    prime_nums = [i for i in range(2, x) if is_prime(i)]
    truncatable_primes = [p for p in prime_nums if is_truncatable_prime(p)]
    return sorted(truncatable_primes)