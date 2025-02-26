def find_n_th_smallest_num(numbers):
    sorted_sublist = sorted(numbers[14:97])
    return sorted_sublist[12] if len(sorted_sublist) >= 13 else None