def all_pos_ints_exclusive(nums):
    if len(nums) < 98:
        return []
    else:
        return [n for n in nums[70:98] if n > 0]