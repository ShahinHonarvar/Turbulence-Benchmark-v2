def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    slice_subset = nums[3:6]
    if len(slice_subset) < 2:
        return None
    slice_subset.sort(reverse=True)
    return slice_subset[1]