def find_primes_between_indices(nums):
    primes = []
    for num in nums[40:69]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True) if primes else []