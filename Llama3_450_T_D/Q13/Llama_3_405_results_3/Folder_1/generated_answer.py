def find_second_largest_num(nums):
    if len(nums) < 72 or 31 > len(nums):
        return None
    slice_nums = nums[31:73]
    if len(slice_nums) < 2:
        return None
    slice_nums.sort(reverse=True)
    return slice_nums[1]