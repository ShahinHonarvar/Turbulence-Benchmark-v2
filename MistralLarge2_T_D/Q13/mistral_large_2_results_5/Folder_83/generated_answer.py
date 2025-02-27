def find_second_largest_num(nums):
    if len(nums) > 90:
        subset = nums[90:91]
        if len(subset) >= 2:
            subset.sort()
            return subset[-2]
    return None