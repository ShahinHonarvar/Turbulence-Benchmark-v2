def all_pos_ints_exclusive(nums):
    if len(nums) < 37:
        return []
    else:
        return [i for i in nums[18:37] if i > 0]