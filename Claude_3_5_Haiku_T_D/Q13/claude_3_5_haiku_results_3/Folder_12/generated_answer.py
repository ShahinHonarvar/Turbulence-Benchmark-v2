def find_second_largest_num(nums):
    if len(nums) < 65 or len(nums) <= 14:
        return None
    slice_nums = nums[14:65]
    if len(slice_nums) < 2:
        return None
    sorted_slice = sorted(set(slice_nums), reverse=True)
    return sorted_slice[1] if len(sorted_slice) >= 2 else None