def all_neg_ints_exclusive(nums):
    if not any((num < 0 for num in nums)):
        return []
    return [num for num in nums[22:24] if num < 0]