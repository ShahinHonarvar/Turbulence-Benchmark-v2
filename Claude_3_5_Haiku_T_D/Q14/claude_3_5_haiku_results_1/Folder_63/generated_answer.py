def find_second_smallest_num(nums):
    if len(nums) <= 82:
        return None
    subset = nums[56:83]
    if len(subset) < 2:
        return None
    unique_subset = sorted(set(subset))
    if len(unique_subset) < 2:
        return None
    return unique_subset[1]