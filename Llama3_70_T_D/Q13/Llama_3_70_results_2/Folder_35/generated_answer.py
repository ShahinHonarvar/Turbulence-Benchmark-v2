def find_second_largest_num(nums):
    if len(nums) < 49:
        return None
    slice_nums = sorted(nums[30:49])
    if len(slice_nums) < 2:
        return None
    return slice_nums[-2]