def all_pos_ints_inclusive(nums):
    if len(nums) < 60:
        return []
    return [n for n in nums[25:60] if n > 0]