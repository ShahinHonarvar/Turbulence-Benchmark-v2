def all_neg_ints_inclusive(nums):
    if not any((num < 0 for num in nums[686:988])):
        return []
    return [num for num in nums[686:988] if num < 0]