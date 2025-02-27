def find_second_largest_num(nums):
    if len(nums) < 93 or len(nums) < 62:
        return None
    sub_nums = nums[62:93]
    if len(set(sub_nums)) < 2:
        return None
    return sorted(sub_nums)[-2]