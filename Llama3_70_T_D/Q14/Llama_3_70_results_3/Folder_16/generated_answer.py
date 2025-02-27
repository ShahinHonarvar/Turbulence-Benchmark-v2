def find_second_smallest_num(nums):
    if len(nums) < 78:
        return None
    slice_nums = sorted(nums[66:78])
    if len(slice_nums) < 2:
        return None
    return slice_nums[1]