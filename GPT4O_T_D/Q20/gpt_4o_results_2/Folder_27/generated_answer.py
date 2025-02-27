def find_n_th_smallest_num(nums):
    sub_list = sorted(nums[75:92])
    return sub_list[10] if len(sub_list) >= 11 else None