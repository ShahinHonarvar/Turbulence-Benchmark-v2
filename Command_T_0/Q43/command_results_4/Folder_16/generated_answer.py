def find_primes_between_indices(nums):
    primes = []
    for i in range(424, 552 + 1):
        if all((nums[i] % k != 0 for k in range(2, int(nums[i] ** 0.5) + 1))):
            primes.append(nums[i])
    return sorted(primes)