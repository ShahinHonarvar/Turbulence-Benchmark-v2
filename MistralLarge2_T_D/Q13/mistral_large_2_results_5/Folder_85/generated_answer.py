def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    subset = sorted(nums[6:9])
    if len(subset) < 2:
        return None
    return subset[-2]