def all_pos_ints_inclusive(nums):
    if len(nums) < 75:
        return []
    return [n for n in nums[75:95] if n > 0]