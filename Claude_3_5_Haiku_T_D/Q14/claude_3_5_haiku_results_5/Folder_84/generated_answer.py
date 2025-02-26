def find_second_smallest_num(nums):
    if not nums or len(nums) <= 40:
        return None
    slice_range = nums[40:81]
    if len(slice_range) < 2:
        return None
    sorted_slice = sorted(set(slice_range))
    return sorted_slice[1] if len(sorted_slice) >= 2 else None