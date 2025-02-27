def find_second_smallest_num(nums):
    if 746 >= len(nums) or 262 >= len(nums) or 746 < 262:
        return None
    sliced_nums = sorted(nums[262:747])
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]