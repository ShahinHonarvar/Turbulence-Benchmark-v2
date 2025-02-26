def find_n_th_smallest_num(numbers):
    sublist = numbers[47:90]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[6] if len(sorted_sublist) >= 7 else None