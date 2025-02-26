def all_pos_ints_exclusive(nums):
    if len(nums) <= 70 or len(nums) <= 98:
        return []
    positive_ints = [num for num in nums[71:98] if num > 0]
    return positive_ints