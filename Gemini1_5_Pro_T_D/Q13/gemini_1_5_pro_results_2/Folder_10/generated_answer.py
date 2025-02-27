def find_second_largest_num(nums):
    if len(nums) < 60:
        return None
    sub_nums = nums[25:60]
    if len(set(sub_nums)) < 2:
        return None
    return sorted(sub_nums)[-2]