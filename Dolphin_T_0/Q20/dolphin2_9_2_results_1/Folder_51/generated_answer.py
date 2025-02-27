def find_n_th_smallest_num(lst):
    if len(lst) < 9:
        return 'Invalid input'
    return sorted(lst)[7]