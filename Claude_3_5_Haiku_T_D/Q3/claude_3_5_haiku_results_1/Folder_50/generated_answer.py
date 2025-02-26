def all_pos_ints_inclusive(nums):
    if len(nums) <= 84:
        return []
    positive_ints = [num for num in nums[70:85] if num > 0]
    return positive_ints