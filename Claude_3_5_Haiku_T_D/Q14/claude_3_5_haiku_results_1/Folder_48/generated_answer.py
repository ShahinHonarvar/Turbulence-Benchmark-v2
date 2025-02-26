def find_second_smallest_num(nums):
    if len(nums) < 248:
        return None
    slice_nums = nums[246:751]
    if len(slice_nums) < 2:
        return None
    sorted_slice = sorted(set(slice_nums))
    return sorted_slice[1] if len(sorted_slice) >= 2 else None