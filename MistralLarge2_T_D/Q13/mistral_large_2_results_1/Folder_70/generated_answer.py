def find_second_largest_num(nums):
    if len(nums) <= 32:
        return None
    subset = sorted(nums[28:33])
    if len(subset) < 2:
        return None
    return subset[-2]