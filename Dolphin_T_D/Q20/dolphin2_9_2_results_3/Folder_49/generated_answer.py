def find_n_th_smallest_num(numbers_list):
    sublist = numbers_list[20:201]
    sublist.sort()
    return sublist[10]