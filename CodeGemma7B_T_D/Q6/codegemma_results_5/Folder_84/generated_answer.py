def all_neg_ints_exclusive(nums):
    if not any((num < 0 for num in nums[50:93])):
        return []
    return [num for num in nums[50:93] if num < 0]