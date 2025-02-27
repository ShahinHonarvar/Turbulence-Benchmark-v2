def find_second_largest_num(nums):
    if len(nums) < 88:
        return None
    subset = nums[25:88]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]