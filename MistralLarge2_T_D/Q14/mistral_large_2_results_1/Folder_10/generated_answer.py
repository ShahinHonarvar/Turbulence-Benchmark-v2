def find_second_smallest_num(nums):
    if len(nums) < 93:
        return None
    subset = nums[62:93]
    unique_subset = list(set(subset))
    if len(unique_subset) < 2:
        return None
    unique_subset.sort()
    return unique_subset[1]