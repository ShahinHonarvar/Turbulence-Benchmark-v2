def all_pos_ints_inclusive(nums):
    if len(nums) <= 55:
        return []
    return [num for num in nums[27:56] if num > 0]