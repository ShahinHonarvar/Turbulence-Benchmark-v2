def all_pos_ints_exclusive(nums):
    if len(nums) <= 45:
        return []
    subset = nums[45:78]
    return [num for num in subset if num > 0]