def find_n_th_smallest_num(nums):
    sub_list = nums[299:636]
    sub_list.sort()
    return sub_list[11]