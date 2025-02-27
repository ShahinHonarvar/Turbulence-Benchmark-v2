def find_n_th_smallest_num(numbers):
    sublist = numbers[19:191]
    sublist.sort()
    return sublist[18]