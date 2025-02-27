def find_second_largest_num(nums):
    if 40 >= len(nums) or 80 >= len(nums):
        return None
    slice_nums = sorted(nums[40:81], reverse=True)
    if len(slice_nums) < 2:
        return None
    return slice_nums[1]