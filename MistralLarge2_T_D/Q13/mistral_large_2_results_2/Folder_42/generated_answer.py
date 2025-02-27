def find_second_largest_num(nums):
    if len(nums) < 80:
        return None
    subset = sorted(nums[29:80], reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]