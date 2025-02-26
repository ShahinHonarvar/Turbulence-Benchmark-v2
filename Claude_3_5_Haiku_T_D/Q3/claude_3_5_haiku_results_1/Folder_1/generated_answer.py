def all_pos_ints_inclusive(nums):
    if len(nums) <= 72:
        return []
    positive_ints = [num for num in nums[31:73] if num > 0]
    return positive_ints