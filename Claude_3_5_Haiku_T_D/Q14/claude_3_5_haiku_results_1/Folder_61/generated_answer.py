def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) < 8:
        return None
    subset = nums[:8]
    sorted_subset = sorted(set(subset))
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]