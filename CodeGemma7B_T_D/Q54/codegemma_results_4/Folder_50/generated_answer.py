from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def right_trunc_prime(n):
    if is_prime(n):
        for i in reversed(range(1, len(str(n)))):
            if not is_prime(int(str(n)[:-i])):
                return False
        return True
    return False

def all_right_truncatable_prime(nums):
    x = nums[57]
    primes = []
    for i in range(2, x):
        if is_prime(i) and right_trunc_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)