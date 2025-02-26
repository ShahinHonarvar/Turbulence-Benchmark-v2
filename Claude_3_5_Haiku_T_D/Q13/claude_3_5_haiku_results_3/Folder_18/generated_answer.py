def find_second_largest_num(nums):
    if len(nums) < 50:
        return None
    slice_nums = nums[35:50]
    if len(slice_nums) == 0:
        return None
    sorted_slice = sorted(set(slice_nums), reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None