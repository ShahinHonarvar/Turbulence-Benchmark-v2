def find_n_th_smallest_num(numbers):
    sublist = numbers[11:44]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[15] if len(sorted_sublist) >= 16 else None