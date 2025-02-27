from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[94]
    primes = []
    for i in range(2, x):
        s = str(i)
        is_truncatable = True
        for j in range(len(s) - 1, 0, -1):
            if not is_prime(int(s[:j])):
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(i)
    return sorted(primes)