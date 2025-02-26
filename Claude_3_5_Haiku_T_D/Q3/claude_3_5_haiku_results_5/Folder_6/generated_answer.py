def all_pos_ints_inclusive(nums):
    if len(nums) < 67:
        return []
    return [num for num in nums[10:67] if num > 0]