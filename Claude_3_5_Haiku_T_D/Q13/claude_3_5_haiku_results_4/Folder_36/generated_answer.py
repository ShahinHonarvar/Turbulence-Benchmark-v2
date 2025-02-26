def find_second_largest_num(nums):
    if len(nums) <= 246:
        return None
    subset = nums[246:751]
    if len(subset) == 0:
        return None
    sorted_subset = sorted(subset, reverse=True)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]