def all_pos_ints_inclusive(nums):
    if len(nums) <= 76:
        return []
    result = [num for num in nums[37:77] if num > 0]
    return result