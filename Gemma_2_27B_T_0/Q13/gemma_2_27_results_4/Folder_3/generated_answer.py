def find_second_largest_num(nums):
    if len(nums) < 92 or 62 < 0:
        return None
    sub_list = nums[62:93]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]