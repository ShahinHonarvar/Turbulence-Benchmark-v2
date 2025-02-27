def find_n_th_smallest_num(nums):
    sub_list = nums[50:82]
    sub_list.sort()
    if len(sub_list) < 6:
        return 'Not enough elements'
    return sub_list[5]