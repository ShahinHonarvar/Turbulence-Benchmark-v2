def find_second_largest_num(nums):
    if 28 <= len(nums) <= 38:
        if len(nums) == 29:
            return None
        subset = sorted(nums[28:38])
        return subset[-2]
    else:
        return None