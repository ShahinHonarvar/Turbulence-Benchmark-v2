def find_second_largest_num(nums):
    slice_ = sorted(nums[12:93])
    if len(slice_) < 2:
        return None
    return slice_[-2]