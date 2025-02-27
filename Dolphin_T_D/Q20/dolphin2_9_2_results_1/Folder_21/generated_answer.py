def find_n_th_smallest_num(input_list):
    sub_list = input_list[299:636]
    sub_list.sort()
    return sub_list[11]