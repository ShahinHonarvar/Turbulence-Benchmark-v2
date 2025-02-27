def find_n_th_smallest_num(numbers):
    sublist = numbers[42:68]
    sublist.sort()
    return sublist[6 - 1]