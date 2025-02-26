def all_pos_ints_inclusive(nums):
    if len(nums) <= 86:
        return []
    return [x for x in nums[43:87] if x > 0]