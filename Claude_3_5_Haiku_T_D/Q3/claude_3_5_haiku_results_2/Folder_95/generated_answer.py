def all_pos_ints_inclusive(nums):
    if len(nums) <= 86:
        return []
    result = [num for num in nums[82:87] if num > 0]
    return result