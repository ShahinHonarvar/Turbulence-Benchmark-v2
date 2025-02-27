def find_n_th_smallest_num(lst):
    subset = sorted(lst[30:99])
    if len(subset) < 5:
        return 'List is too small to have a 5th smallest element'
    else:
        return subset[4]