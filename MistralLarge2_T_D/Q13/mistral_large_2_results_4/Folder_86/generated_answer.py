def find_second_largest_num(nums):
    subset = nums[31:35]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]