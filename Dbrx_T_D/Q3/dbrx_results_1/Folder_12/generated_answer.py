def all_pos_ints_inclusive(nums):
    if len(nums) < 65:
        return []
    else:
        return [n for n in nums[14:65] if n > 0]