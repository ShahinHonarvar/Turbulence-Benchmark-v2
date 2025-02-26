def find_second_smallest_num(nums):
    if len(nums) <= 39:
        return None
    slice_subset = nums[15:40]
    if len(slice_subset) < 2:
        return None
    sorted_subset = sorted(set(slice_subset))
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]