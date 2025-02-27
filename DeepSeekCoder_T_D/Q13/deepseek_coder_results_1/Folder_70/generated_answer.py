def find_second_largest_num(nums):
    if len(nums) < 33:
        return None
    sub_list = sorted(nums[28:33])
    if len(sub_list) < 2:
        return None
    return sub_list[-2]