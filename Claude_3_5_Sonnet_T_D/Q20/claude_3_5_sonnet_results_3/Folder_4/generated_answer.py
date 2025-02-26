def find_n_th_smallest_num(numbers):
    sublist = numbers[34:95]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[17] if len(sorted_sublist) >= 18 else None