def find_second_largest_num(nums):
    if len(nums) < 51:
        return None
    slice_range = nums[22:51]
    if len(slice_range) < 2:
        return None
    sorted_slice = sorted(set(slice_range), reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None