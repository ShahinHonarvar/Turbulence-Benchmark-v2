def find_second_largest_num(nums):
    if len(nums) < 37:
        return None
    subset = nums[33:37]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]