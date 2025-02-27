def find_second_largest_num(nums):
    if len(nums) < 65:
        return None
    subset = sorted(nums[14:65])
    if len(subset) < 2:
        return None
    return subset[-2]