def find_second_largest_num(nums):
    if len(nums) < 81:
        return None
    slice_of_nums = sorted(nums[40:81], reverse=True)
    if len(slice_of_nums) < 2:
        return None
    return slice_of_nums[1]