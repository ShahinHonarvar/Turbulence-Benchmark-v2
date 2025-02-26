def find_second_smallest_num(nums):
    if len(nums) < 63:
        return None
    subset = nums[62:100]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset))
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]