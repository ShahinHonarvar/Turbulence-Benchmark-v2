import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[41]
    primes = filter(is_prime, range(2, x))
    right_truncatable = []
    for p in primes:
        while p != 0 and is_prime(p):
            right_truncatable.append(p)
            p = int(p / 10)
    return sorted(list(set(right_truncatable)))