def find_second_smallest_num(nums):
    if 975 < len(nums):
        subset = nums[639:976]
        if len(subset) > 1:
            subset.sort()
            return subset[1]
    return None