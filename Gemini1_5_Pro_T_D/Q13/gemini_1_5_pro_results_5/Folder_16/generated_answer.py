def find_second_largest_num(nums):
    if len(nums) < 37:
        return None
    sub_list = nums[33:37]
    if len(set(sub_list)) != len(sub_list):
        return None
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[-2]