def find_second_largest_num(nums):
    if len(nums) <= 74 or len(nums) <= 95:
        return None
    subset = nums[74:96]
    if len(subset) < 2:
        return None
    subset = sorted(subset, reverse=True)
    return subset[1]