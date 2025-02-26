def all_pos_ints_inclusive(nums):
    if len(nums) <= 200:
        return []
    positive_ints = [num for num in nums[60:201] if num > 0]
    return positive_ints