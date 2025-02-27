def find_second_smallest_num(nums):
    subset = sorted(nums[639:976])
    if len(subset) < 2:
        return None
    return subset[1]