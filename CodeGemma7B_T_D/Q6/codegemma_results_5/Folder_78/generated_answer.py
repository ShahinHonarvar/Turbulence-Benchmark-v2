def all_neg_ints_exclusive(nums):
    if any((num < 0 for num in nums[20:35])):
        return [num for num in nums[20:35] if num < 0]
    else:
        return []