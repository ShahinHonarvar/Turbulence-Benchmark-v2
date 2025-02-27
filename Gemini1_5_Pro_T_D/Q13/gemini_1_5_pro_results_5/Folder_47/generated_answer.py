def find_second_largest_num(nums):
    if len(nums) < 77:
        return None
    sub_nums = nums[37:77]
    if len(set(sub_nums)) < 2:
        return None
    return sorted(sub_nums)[-2]