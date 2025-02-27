def find_second_smallest_num(lst):
    sublist = lst[56:83]
    if len(sublist) < 2:
        return None
    sublist_sorted = sorted(sublist)
    return sublist_sorted[1]