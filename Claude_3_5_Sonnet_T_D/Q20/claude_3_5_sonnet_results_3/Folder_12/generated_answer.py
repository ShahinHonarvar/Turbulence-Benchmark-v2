def find_n_th_smallest_num(numbers):
    sublist = numbers[40:69]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[13] if len(sorted_sublist) >= 14 else None