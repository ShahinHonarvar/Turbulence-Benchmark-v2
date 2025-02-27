def find_n_th_smallest_num(nums):
    sub_list = nums[106:255]
    sub_list.sort()
    if len(sub_list) >= 9:
        return sub_list[8]
    return None