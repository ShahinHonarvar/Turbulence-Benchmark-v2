def find_second_largest_num(nums):
    if 90 < len(nums) < 90:
        subset = nums[90:91]
        if len(subset) > 1:
            subset.sort()
            return subset[1]
    return None