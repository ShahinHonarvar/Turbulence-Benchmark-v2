def find_primes_between_indices(nums):
    primes = []
    for i in range(66, 82):
        if is_prime(nums[i]):
            primes.append(nums[i])
    primes.sort()
    return primes