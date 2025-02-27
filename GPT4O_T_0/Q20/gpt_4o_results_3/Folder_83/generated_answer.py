def find_n_th_smallest_num(numbers):
    sublist = numbers[30:301]
    sublist.sort()
    return sublist[14]