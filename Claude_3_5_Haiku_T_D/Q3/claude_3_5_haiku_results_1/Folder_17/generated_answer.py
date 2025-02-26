def all_pos_ints_inclusive(nums):
    if len(nums) <= 78:
        return []
    result = [num for num in nums[62:79] if num > 0]
    return result