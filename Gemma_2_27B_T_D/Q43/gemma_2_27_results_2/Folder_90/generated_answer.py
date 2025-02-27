def find_primes_between_indices(nums):
    primes = []
    for i in range(413, 449):
        if i < len(nums) and all((nums[i] % j for j in range(2, int(nums[i] ** 0.5) + 1))) and (nums[i] > 1):
            primes.append(nums[i])
    return sorted(primes)