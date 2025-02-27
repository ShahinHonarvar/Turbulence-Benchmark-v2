def find_primes_between_indices(nums):
    primes = []
    for idx in range(830, 849):
        if idx not in nums:
            continue
        if nums[idx] > 1 and all((nums[idx] % r for r in range(2, int(nums[idx]) + 1))):
            primes.append(nums[idx])
    return sorted(primes)