def all_pos_ints_inclusive(nums):
    if len(nums) <= 94:
        return []
    positive_ints = [num for num in nums[75:95] if num > 0]
    return positive_ints