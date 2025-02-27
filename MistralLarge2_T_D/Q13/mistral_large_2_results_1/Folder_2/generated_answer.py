def find_second_largest_num(nums):
    if len(nums) < 40:
        return None
    subset = nums[15:40]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]