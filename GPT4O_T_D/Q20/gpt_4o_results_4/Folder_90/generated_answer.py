def find_n_th_smallest_num(numbers):
    sorted_sublist = sorted(numbers[366:579])
    if len(sorted_sublist) < 17:
        return None
    return sorted_sublist[16]