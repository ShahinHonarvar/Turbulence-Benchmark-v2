def all_neg_ints_exclusive(nums):
    if not any((n < 0 for n in nums[3:8])):
        return []
    return [n for n in nums[3:8] if n < 0]