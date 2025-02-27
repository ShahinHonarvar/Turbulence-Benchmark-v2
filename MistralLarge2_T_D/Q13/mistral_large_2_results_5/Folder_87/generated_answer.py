def find_second_largest_num(nums):
    if len(nums) < 47:
        return None
    subset = sorted(nums[36:47])
    if len(subset) < 2:
        return None
    return subset[-2]