def find_primes_between_indices(nums):
    primes = []
    for num in nums[24:84]:
        if all((num % i for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    return sorted(primes) if primes else []