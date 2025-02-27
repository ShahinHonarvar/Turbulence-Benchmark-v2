def find_second_largest_num(nums):
    slice_nums = sorted(nums[20:201], reverse=True)
    if len(slice_nums) < 2:
        return None
    else:
        return slice_nums[1]