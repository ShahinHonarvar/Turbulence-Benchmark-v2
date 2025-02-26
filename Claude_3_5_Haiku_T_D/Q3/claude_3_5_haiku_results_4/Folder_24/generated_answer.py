def all_pos_ints_inclusive(nums):
    if len(nums) <= 95:
        return []
    result = [num for num in nums[74:96] if num > 0]
    return result