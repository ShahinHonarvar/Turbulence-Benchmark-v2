def find_second_smallest_num(nums):
    subset = sorted(nums[43:87])
    if len(subset) < 2:
        return None
    return subset[1]