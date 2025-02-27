def find_n_th_smallest_num(num_list):
    sublist = num_list[42:81]
    sublist.sort()
    return sublist[5]