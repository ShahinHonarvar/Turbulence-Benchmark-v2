def find_n_th_smallest_num(numbers):
    sublist = numbers[10:101]
    sublist.sort()
    return sublist[9]