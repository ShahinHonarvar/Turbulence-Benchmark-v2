def find_second_largest_num(nums):
    if len(nums) < 28 or len(nums[27:56]) < 2:
        return None
    slice_nums = nums[27:56]
    slice_nums.sort(reverse=True)
    return slice_nums[1]