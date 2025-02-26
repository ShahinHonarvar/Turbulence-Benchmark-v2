def all_pos_ints_inclusive(nums):
    if len(nums) <= 78:
        return []
    positive_ints = [num for num in nums[17:79] if num > 0]
    return positive_ints