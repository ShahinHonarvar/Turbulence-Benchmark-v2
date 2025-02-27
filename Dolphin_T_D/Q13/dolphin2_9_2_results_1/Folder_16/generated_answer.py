def find_second_largest_num(nums):
    sub_list = nums[33:37]
    if len(set(sub_list)) < 2:
        return None
    else:
        sorted_sub_list = sorted(set(sub_list), reverse=True)
        return sorted_sub_list[1]