def all_neg_ints_exclusive(nums):
    if len(nums) < 97:
        return []
    return [n for n in nums[69:97] if n < 0]