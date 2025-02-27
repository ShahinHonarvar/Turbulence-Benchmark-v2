def find_second_largest_num(nums):
    sub_list = nums[43:52]
    if len(sub_list) >= 2:
        return sorted(sub_list)[-2]
    else:
        return None