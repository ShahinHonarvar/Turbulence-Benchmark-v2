def find_second_largest_num(nums):
    if len(nums) < 36:
        return None
    subset = nums[32:36]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]