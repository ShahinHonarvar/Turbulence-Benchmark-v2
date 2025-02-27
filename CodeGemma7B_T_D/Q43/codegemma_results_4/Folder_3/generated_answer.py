def find_primes_between_indices(nums):
    primes = []
    for i in range(80, 85):
        if is_prime(nums[i]):
            primes.append(nums[i])
    primes.sort(reverse=True)
    return primes