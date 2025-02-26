def find_n_th_smallest_num(numbers):
    sorted_sublist = sorted(numbers[21:70])
    return sorted_sublist[9] if len(sorted_sublist) >= 10 else None