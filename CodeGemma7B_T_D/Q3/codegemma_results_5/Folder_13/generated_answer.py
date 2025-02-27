def all_pos_ints_inclusive(nums):
    if max(nums) <= 0 or min(nums) > 88:
        return []
    return nums[25:88 + 1]