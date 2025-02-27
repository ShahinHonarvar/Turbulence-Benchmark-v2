def find_second_smallest_num(nums):
    slice_nums = nums[62:93]
    if len(slice_nums) < 2:
        return None
    else:
        slice_nums.sort()
        return slice_nums[1]