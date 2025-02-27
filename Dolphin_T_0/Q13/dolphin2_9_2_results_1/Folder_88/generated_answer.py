def find_second_largest_num(nums):
    subset = nums[4:9]
    if len(set(subset)) < 2:
        return None
    else:
        subset.sort()
        return subset[-2]