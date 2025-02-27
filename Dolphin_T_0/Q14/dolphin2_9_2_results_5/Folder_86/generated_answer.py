def find_second_smallest_num(lst):
    if len(lst) >= 36:
        sublist = lst[33:37]
        sublist_sorted = sorted(sublist)
        if len(sublist_sorted) >= 2:
            return sublist_sorted[1]
    return None