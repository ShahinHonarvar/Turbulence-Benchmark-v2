def find_n_th_smallest_num(lst):
    if not lst or len(lst) < 17:
        return None
    lst = sorted(lst)
    return lst[16]