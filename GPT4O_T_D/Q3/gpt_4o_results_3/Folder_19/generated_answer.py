def all_pos_ints_inclusive(nums):
    if len(nums) < 6:
        return []
    return [num for num in nums[3:6] if num > 0]