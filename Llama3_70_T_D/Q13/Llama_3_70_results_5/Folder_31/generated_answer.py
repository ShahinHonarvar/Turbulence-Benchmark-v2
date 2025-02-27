def find_second_largest_num(nums):
    if len(nums) < 89:
        return None
    slice_nums = nums[75:89]
    slice_nums.sort(reverse=True)
    if len(slice_nums) < 2:
        return None
    return slice_nums[1]