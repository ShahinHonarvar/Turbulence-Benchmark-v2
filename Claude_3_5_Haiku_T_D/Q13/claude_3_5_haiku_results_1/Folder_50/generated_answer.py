def find_second_largest_num(nums):
    if len(nums) <= 70:
        return None
    slice_nums = nums[70:85]
    if len(slice_nums) < 2:
        return None
    sorted_slice = sorted(set(slice_nums), reverse=True)
    return sorted_slice[1] if len(sorted_slice) >= 2 else None