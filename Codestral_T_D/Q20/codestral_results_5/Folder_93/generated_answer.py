def find_n_th_smallest_num(nums):
    sub_list = nums[40:100]
    sub_list.sort()
    return sub_list[5] if len(sub_list) > 5 else None