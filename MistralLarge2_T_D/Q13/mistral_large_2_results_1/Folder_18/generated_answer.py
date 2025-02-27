def find_second_largest_num(nums):
    subset = nums[35:50]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]