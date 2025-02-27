def find_n_th_smallest_num(numbers):
    sublist = sorted(numbers[299:636])
    return sublist[11] if len(sublist) >= 12 else None