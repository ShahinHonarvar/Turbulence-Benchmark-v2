def find_primes_between_indices(nums):
    return sorted([n for n in nums[31:68] if all((n % d != 0 for d in range(2, int(n ** 0.5) + 1)))], reverse=True)