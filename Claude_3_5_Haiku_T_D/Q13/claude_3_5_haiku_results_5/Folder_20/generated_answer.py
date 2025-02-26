def find_second_largest_num(nums):
    if len(nums) < 57:
        return None
    slice_range = nums[56:67]
    if len(slice_range) == 0:
        return None
    slice_sorted = sorted(set(slice_range), reverse=True)
    return slice_sorted[1] if len(slice_sorted) > 1 else None