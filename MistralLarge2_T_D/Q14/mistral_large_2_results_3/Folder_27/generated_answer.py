def find_second_smallest_num(lst):
    if len(lst) < 60:
        return None
    sublist = lst[25:60]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]