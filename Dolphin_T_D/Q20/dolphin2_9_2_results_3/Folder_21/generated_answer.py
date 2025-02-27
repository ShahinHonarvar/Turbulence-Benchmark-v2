def find_n_th_smallest_num(lst):
    substr = lst[299:636]
    substr.sort()
    return substr[11]