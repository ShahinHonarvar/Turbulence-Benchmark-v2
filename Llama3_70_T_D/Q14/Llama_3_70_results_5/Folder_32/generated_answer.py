def find_second_smallest_num(lst):
    if len(lst) < 36:
        return None
    sublist = lst[32:36]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]