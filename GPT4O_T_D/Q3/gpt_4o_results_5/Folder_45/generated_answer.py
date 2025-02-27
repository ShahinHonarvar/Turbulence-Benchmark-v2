def all_pos_ints_inclusive(nums):
    if len(nums) < 31:
        return []
    return [num for num in nums[30:201] if num > 0]