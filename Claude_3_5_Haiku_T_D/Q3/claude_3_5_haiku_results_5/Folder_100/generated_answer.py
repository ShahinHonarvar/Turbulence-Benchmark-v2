def all_pos_ints_inclusive(nums):
    if len(nums) <= 68:
        return []
    subset = nums[42:69]
    return [num for num in subset if num > 0]