def all_pos_ints_inclusive(nums):
    if len(nums) < 5:
        return []
    result = [num for num in nums[4:5] if num > 0]
    return result