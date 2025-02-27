def find_second_largest_num(nums):
    slice_nums = nums[62:79]
    sorted_nums = sorted(slice_nums, reverse=True)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]