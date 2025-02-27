def find_second_largest_num(nums):
    if len(nums) < 89:
        return None
    slice_ = sorted(nums[75:89], reverse=True)
    if len(slice_) < 2:
        return None
    return slice_[1]