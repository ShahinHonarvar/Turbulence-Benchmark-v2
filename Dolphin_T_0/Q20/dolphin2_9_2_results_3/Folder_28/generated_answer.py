def find_n_th_smallest_num(lst):
    sublist = sorted(lst[57:94])
    if len(sublist) > 11:
        return sublist[11]
    else:
        return 'Not enough elements'