def all_pos_ints_inclusive(nums):
    if len(nums) < 56:
        return []
    result = [num for num in nums[34:56] if num > 0]
    return result