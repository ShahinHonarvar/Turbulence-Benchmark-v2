def composite_nums_between_indices(nums):
    return set((num for num in nums[43:87] if num > 1 and (not any((num % div == 0 for div in range(2, int(num ** 0.5) + 1))))))