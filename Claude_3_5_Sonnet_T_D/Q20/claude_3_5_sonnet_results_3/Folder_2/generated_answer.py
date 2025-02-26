def find_n_th_smallest_num(numbers):
    sublist = numbers[23:66]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[7] if len(sorted_sublist) >= 8 else None