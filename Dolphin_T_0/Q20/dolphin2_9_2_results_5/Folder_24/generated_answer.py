def find_n_th_smallest_num(numbers_list):
    sublist = numbers_list[42:81]
    sublist.sort()
    return sublist[5]