def find_second_largest_num(nums):
    subset = sorted(set(nums[37:77]))
    return subset[-2] if len(subset) > 1 else None