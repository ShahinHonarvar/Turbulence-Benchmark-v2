from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[61]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            is_left_truncatable = True
            n = str(i)
            for j in range(1, len(n)):
                if not is_prime(int(n[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    return sorted(primes)