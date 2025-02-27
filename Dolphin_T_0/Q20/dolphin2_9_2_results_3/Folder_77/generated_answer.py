def find_n_th_smallest_num(numbers):
    sublist = numbers[105:255]
    sublist.sort()
    return sublist[8]