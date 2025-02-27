def all_neg_ints_exclusive(nums):
    if any((num < 0 for num in nums[55:84])):
        return [num for num in nums[55:84] if num < 0]
    else:
        return []