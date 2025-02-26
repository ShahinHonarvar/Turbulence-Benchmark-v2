def all_pos_ints_inclusive(nums):
    if len(nums) <= 98:
        return []
    result = [num for num in nums[55:99] if num > 0]
    return result