def find_second_smallest_num(lst):
    if len(lst) < 64:
        return None
    sublist = lst[22:64]
    sublist_sorted = sorted(sublist)
    if len(sublist_sorted) < 2:
        return None
    return sublist_sorted[1]