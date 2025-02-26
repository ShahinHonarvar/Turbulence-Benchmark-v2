def find_second_largest_num(nums):
    if len(nums) <= 10:
        return None
    slice_nums = nums[10:101]
    if len(slice_nums) == 0:
        return None
    sorted_slice = sorted(slice_nums, reverse=True)
    return sorted_slice[1] if len(sorted_slice) >= 2 else None