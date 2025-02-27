from math import trunc

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, trunc(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[36]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            is_truncatable = True
            while j > 0:
                if not is_prime(j):
                    is_truncatable = False
                    break
                j //= 10
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)