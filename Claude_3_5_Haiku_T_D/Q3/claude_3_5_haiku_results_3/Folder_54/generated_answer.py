def all_pos_ints_inclusive(nums):
    if len(nums) <= 55:
        return []
    positive_subset = [num for num in nums[34:56] if num > 0]
    return positive_subset