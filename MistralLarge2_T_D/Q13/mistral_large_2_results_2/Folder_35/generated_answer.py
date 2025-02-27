def find_second_largest_num(nums):
    if len(nums) < 49:
        return None
    subset = sorted(nums[30:49], reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]