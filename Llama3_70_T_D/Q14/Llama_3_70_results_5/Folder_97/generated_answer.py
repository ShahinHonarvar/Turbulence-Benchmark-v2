def find_second_smallest_num(nums):
    if len(nums) < 35:
        return None
    slice_nums = sorted(nums[31:35])
    if len(slice_nums) < 2 or slice_nums[0] == slice_nums[1]:
        return None
    return slice_nums[1]