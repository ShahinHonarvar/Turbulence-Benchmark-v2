def find_second_largest_num(nums):
    if len(nums) < 33:
        return None
    subset = sorted(nums[28:33], reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]