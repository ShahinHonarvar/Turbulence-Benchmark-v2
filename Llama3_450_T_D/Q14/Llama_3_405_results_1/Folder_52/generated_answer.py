def find_second_smallest_num(nums):
    if len(nums) < 67:
        return None
    slice_nums = nums[64:67]
    set_nums = set(slice_nums)
    if len(set_nums) < 2:
        return None
    sorted_nums = sorted(set_nums)
    return sorted_nums[1]