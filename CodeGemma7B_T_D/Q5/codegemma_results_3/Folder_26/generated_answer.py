def all_neg_ints_inclusive(nums):
    if not any((num < 0 for num in nums)):
        return []
    return [num for num in nums[62:100] if num < 0]