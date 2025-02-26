def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    slice_subset = nums[6:9]
    if len(slice_subset) < 2:
        return None
    sorted_subset = sorted(slice_subset)
    return sorted_subset[1]