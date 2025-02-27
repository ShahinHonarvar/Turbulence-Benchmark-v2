def composite_nums_between_indices(nums):
    composites = set((num for num in nums[26:56] if num != 1 and (not is_prime(num))))
    return composites