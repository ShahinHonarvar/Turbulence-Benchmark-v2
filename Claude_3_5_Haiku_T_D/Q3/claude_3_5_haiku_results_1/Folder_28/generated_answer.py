def all_pos_ints_inclusive(nums):
    if len(nums) < 64:
        return []
    pos_ints = [num for num in nums[62:64] if num > 0]
    return pos_ints