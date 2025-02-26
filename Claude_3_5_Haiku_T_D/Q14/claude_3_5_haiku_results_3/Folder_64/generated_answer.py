def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    slice_sub = nums[0:5]
    if len(slice_sub) < 2:
        return None
    sorted_slice = sorted(slice_sub)
    return sorted_slice[1]