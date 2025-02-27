def find_n_th_smallest_num(lst):
    part = sorted(lst[50:71])
    return part[8] if len(part) > 9 else None