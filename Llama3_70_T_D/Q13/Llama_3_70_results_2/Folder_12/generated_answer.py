def find_second_largest_num(nums):
    slice_of_nums = nums[14:65]
    if len(slice_of_nums) < 2:
        return None
    slice_of_nums.sort(reverse=True)
    return slice_of_nums[1]