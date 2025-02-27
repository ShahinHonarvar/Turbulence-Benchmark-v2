def find_n_th_smallest_num(list_num):
    lst = list_num[35:61]
    lst.sort(key=int)
    return lst[3]