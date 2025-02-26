def all_pos_ints_inclusive(nums):
    if len(nums) <= 82:
        return []
    result = [num for num in nums[56:83] if num > 0]
    return result