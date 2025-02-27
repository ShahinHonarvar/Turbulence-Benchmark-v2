def find_primes_between_indices(nums):
    return sorted([num for num in nums[28:37] if all((num % i for i in range(2, int(num ** 0.5) + 1))) and num > 1])