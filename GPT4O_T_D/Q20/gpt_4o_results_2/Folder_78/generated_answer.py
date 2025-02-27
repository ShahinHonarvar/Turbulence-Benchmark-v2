def find_n_th_smallest_num(numbers):
    sorted_sublist = sorted(numbers[16:72])
    if len(sorted_sublist) < 14:
        return None
    return sorted_sublist[13]