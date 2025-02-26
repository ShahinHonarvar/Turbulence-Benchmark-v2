def all_pos_ints_inclusive(nums):
    if len(nums) <= 987:
        return []
    result = [num for num in nums[686:988] if num > 0]
    return result