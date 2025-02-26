def find_second_smallest_num(nums):
    if len(nums) < 79:
        return None
    subset = nums[62:79]
    if len(subset) < 2:
        return None
    unique_subset = sorted(set(subset))
    if len(unique_subset) < 2:
        return None
    return unique_subset[1]