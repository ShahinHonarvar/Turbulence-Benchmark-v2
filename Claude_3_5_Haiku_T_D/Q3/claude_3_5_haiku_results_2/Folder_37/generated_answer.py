def all_pos_ints_inclusive(nums):
    if len(nums) < 6:
        return []
    result = [num for num in nums[1:6] if num > 0]
    return result