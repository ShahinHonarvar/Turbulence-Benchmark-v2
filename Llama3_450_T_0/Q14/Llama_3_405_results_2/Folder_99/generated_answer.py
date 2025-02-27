def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    slice_nums = nums[608:610]
    sorted_nums = sorted(slice_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]