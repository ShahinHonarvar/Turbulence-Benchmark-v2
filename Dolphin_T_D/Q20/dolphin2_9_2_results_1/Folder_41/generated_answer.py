def find_n_th_smallest_num(lst):
    if not isinstance(lst, list) or len(lst) < 5:
        return 'Error: List should contain at least 5 numbers.'
    sublst = lst[4:9] if len(lst) > 8 else lst[4:]
    sublst.sort()
    return sublst[3]