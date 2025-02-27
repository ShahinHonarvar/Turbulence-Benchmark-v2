def find_n_th_smallest_num(numbers):
    sublist = numbers[0:6]
    sublist.sort()
    return sublist[5]