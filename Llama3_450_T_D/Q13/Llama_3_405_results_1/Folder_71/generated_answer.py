def find_second_largest_num(nums):
    if len(nums) < 53:
        return None
    slice_nums = nums[26:53]
    if len(slice_nums) < 2:
        return None
    slice_nums.sort()
    return slice_nums[-2]