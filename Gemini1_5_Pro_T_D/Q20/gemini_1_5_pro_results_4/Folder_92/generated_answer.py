def find_n_th_smallest_num(numbers):
    sublist = numbers[:4]
    sublist.sort()
    return sublist[3]