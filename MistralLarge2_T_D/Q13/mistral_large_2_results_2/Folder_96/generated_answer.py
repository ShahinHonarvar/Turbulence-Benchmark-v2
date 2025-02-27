def find_second_largest_num(nums):
    if len(nums) <= 51:
        return None
    subset = nums[15:52]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]