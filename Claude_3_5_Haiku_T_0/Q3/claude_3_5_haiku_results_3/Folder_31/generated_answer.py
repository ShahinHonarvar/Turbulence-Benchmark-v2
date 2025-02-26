def all_pos_ints_inclusive(nums):
    if len(nums) <= 88:
        return []
    result = [num for num in nums[75:89] if num > 0]
    return result