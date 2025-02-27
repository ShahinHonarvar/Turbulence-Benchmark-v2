def find_primes_between_indices(nums):
    primes = []
    for i in range(13, 30):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(nums[i])
    return sorted(primes, reverse=True) if primes else []