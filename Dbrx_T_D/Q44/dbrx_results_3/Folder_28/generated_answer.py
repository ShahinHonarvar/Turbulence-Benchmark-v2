def composite_nums_between_indices(nums):
    return set((num for num in nums[22:89] if num > 1 and (not any((num % i == 0 for i in range(2, num))))))