def find_primes_between_indices(nums):
    primes = []
    for i in range(459, 782):
        num = nums[i]
        if is_prime(num):
            primes.append(num)
    primes.sort()
    return primes if primes else []

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True