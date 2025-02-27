def all_pos_ints_inclusive(nums):
    if len(nums) < 92:
        return []
    elif len(nums) == 92:
        return nums[19:]
    else:
        return nums[19:93]