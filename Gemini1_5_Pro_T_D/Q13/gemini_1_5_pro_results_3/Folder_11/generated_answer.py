def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    sub_nums = nums[37:52]
    if len(set(sub_nums)) < 2:
        return None
    return sorted(sub_nums)[-2]