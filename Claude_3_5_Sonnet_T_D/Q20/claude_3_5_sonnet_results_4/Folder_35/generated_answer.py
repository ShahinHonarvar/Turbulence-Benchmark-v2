def find_n_th_smallest_num(numbers):
    sublist = numbers[12:61]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[5] if len(sorted_sublist) >= 6 else None