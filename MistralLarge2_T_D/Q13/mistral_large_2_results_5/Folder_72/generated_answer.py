def find_second_largest_num(nums):
    if len(nums) <= 51:
        subset = nums[29:52]
        if len(subset) >= 2:
            subset.sort()
            return subset[-2]
    return None