def all_pos_ints_inclusive(nums):
    if len(nums) < 79:
        return []
    return [num for num in nums[62:79] if num > 0]