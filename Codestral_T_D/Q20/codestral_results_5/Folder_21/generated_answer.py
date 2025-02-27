def find_n_th_smallest_num(numbers):
    sublist = numbers[299:636]
    sublist.sort()
    return sublist[11]