def find_second_largest_num(nums):
    if len(nums) < 79:
        return None
    subset = sorted(nums[62:79])
    if len(subset) < 2:
        return None
    return subset[-2]