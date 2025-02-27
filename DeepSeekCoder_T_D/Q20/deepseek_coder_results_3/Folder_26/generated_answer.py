def find_n_th_smallest_num(numbers):
    sublist = sorted(numbers[11:25])
    return sublist[9] if len(sublist) > 9 else None