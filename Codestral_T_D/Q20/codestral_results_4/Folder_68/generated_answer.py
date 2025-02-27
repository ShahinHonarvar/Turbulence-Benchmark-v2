def find_n_th_smallest_num(numbers):
    sublist = numbers[0:11]
    sublist.sort()
    return sublist[10]