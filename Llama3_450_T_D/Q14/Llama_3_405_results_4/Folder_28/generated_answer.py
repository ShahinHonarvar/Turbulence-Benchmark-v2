def find_second_smallest_num(nums):
    slice_ = nums[22:51]
    if len(slice_) < 2:
        return None
    else:
        return sorted(slice_)[1]