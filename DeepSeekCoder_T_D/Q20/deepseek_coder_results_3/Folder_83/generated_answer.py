def find_n_th_smallest_num(numbers):
    sublist = sorted(numbers[30:301])
    return sublist[14] if len(sublist) > 14 else None