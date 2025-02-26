def all_pos_ints_inclusive(nums):
    if len(nums) < 9:
        return []
    pos_ints = [num for num in nums[6:9] if num > 0]
    return pos_ints