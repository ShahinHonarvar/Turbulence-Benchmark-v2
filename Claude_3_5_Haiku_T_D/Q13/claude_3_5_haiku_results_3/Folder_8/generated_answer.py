def find_second_largest_num(nums):
    if len(nums) <= 23:
        return None
    subset = nums[23:24]
    if len(subset) == 0:
        return None
    return subset[0]