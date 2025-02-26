def all_pos_ints_inclusive(nums):
    if len(nums) <= 55:
        return []
    result = [num for num in nums[27:56] if num > 0]
    return result