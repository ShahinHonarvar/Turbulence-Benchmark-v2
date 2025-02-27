def find_second_smallest_num(nums):
    sub_list = nums[37:52]
    if len(sub_list) < 2:
        return None
    else:
        sorted_list = sorted(set(sub_list))
        return sorted_list[1]