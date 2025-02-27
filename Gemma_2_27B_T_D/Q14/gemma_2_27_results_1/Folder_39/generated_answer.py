def find_second_smallest_num(nums):
    sub_list = nums[28:41]
    if len(sub_list) > 1:
        return sorted(sub_list)[1]
    else:
        return None