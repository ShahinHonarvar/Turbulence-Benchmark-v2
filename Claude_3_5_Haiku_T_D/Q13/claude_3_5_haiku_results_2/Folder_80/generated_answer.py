def find_second_largest_num(nums):
    if len(nums) < 67:
        return None
    slice_nums = nums[64:67]
    if len(slice_nums) < 2:
        return None
    sorted_slice = sorted(slice_nums, reverse=True)
    return sorted_slice[1]