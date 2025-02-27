def find_second_largest_num(nums):
    if len(nums) < 2 or 56 >= len(nums) or 98 >= len(nums):
        return None
    slice_nums = nums[56:99]
    if len(slice_nums) < 2:
        return None
    sorted_nums = sorted(slice_nums)
    return sorted_nums[-2]