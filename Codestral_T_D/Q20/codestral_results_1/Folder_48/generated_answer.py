def find_n_th_smallest_num(num_list):
    sub_list = num_list[127:849]
    sub_list.sort()
    if len(sub_list) < 10:
        return 'Not enough elements in the sub-list'
    else:
        return sub_list[9]