def find_second_largest_num(nums):
    subset = sorted(set(nums[310:371]))
    return subset[-2] if len(subset) > 1 else None