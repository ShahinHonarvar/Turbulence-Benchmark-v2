from functools import reduce

def find_factor_set(n):
    fs = {i for i in range(2, n + 1) if n % i == 0}
    return fs if len(fs) == 1 else find_factor_set(n - 1)

def is_prime(n):
    fs = find_factor_set(n)
    return next(fs) == n and len(fs) == 2

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n)) - 1):
        n = int(str(n)[:-i - 1])
        if not is_prime(n):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[803]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])