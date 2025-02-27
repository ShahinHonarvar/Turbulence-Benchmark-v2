def find_second_largest_num(nums):
    if len(nums) < 33:
        return None
    subset = nums[28:33]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]