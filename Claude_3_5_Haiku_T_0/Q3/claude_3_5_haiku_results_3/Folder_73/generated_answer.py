def all_pos_ints_inclusive(nums):
    if len(nums) <= 92:
        return []
    result = [num for num in nums[19:93] if num > 0]
    return result