def all_pos_ints_inclusive(nums):
    if len(nums) <= 40:
        return []
    positive_subset = [num for num in nums[28:41] if num > 0]
    return positive_subset