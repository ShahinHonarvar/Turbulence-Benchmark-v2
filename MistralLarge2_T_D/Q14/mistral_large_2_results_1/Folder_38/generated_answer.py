def find_second_smallest_num(nums):
    subset = nums[37:52]
    if len(subset) < 2:
        return None
    unique_sorted = sorted(set(subset))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]