def find_second_largest_num(nums):
    sub_list = nums[639:976]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[-2]