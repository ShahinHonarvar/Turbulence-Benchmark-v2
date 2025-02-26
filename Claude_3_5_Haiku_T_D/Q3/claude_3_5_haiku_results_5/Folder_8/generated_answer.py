def all_pos_ints_inclusive(nums):
    if len(nums) < 24:
        return []
    result = [num for num in nums[23:24] if num > 0]
    return result