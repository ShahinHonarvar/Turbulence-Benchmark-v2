def all_neg_ints_exclusive(nums):
    if len(nums) > 2:
        return [x for x in nums[1:-1] if x < 0]
    return []