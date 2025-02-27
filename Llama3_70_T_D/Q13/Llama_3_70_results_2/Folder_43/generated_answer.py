def find_second_largest_num(nums):
    slice_nums = nums[68:87]
    if len(slice_nums) < 2:
        return None
    slice_nums.sort(reverse=True)
    return slice_nums[1]