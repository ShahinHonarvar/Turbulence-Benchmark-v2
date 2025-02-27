def find_n_th_smallest_num(numbers):
    sublist = numbers[10:101]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[9]