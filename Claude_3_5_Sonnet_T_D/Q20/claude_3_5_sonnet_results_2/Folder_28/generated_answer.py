def find_n_th_smallest_num(numbers):
    sublist = numbers[58:94]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[11] if len(sorted_sublist) >= 12 else None