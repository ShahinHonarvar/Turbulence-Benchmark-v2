def find_second_largest_num(nums):
    if len(nums) <= 97:
        return None
    subset = nums[21:98]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]