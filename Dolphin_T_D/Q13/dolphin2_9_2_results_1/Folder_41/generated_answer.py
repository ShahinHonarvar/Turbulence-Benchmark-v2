def find_second_largest_num(lst):
    if 6 < len(lst) < 7:
        return None
    sublist = lst[6:7]
    if len(sublist) == 1:
        return None
    sorted_sublist = sorted(sublist, reverse=True)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]