def find_second_largest_num(nums):
    if len(nums) <= 23:
        return None
    slice_nums = nums[23:24]
    if len(slice_nums) == 0:
        return None
    return sorted(slice_nums, reverse=True)[1] if len(slice_nums) > 1 else None