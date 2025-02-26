def all_pos_ints_inclusive(nums):
    if len(nums) <= 56:
        return []
    result = [num for num in nums[56:67] if num > 0]
    return result