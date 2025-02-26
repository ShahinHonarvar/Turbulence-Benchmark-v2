def all_pos_ints_inclusive(nums):
    if len(nums) <= 975:
        return []
    subset = nums[639:976]
    return [num for num in subset if num > 0]