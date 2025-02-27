def find_second_largest_num(nums):
    if len(nums) < 79 or 17 > len(nums):
        return None
    slice_nums = nums[17:79]
    if len(slice_nums) < 2:
        return None
    return sorted(slice_nums)[-2]