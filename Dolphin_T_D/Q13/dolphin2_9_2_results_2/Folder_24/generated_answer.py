def find_second_largest_num(nums):
    slice_nums = nums[73:96]
    if len(slice_nums) >= 2:
        slice_nums = list(set(slice_nums))
        slice_nums.sort()
        return slice_nums[-2]
    else:
        return None