def find_second_smallest_num(nums):
    subset = nums[28:39]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]