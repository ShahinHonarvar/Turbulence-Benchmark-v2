from math import sqrt

def find_primes_between_indices(nums):
    primes = []
    for num in nums[45:81]:
        is_prime = True
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes if primes else []