def find_second_largest_num(nums):
    if len(nums) < 56:
        return None
    slice_list = nums[34:56]
    if len(slice_list) < 2:
        return None
    sorted_slice = sorted(slice_list, reverse=True)
    return sorted_slice[1]