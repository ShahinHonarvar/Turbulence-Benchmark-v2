def all_pos_ints_inclusive(nums):
    if len(nums) <= 97:
        return []
    return [num for num in nums[21:98] if num > 0]