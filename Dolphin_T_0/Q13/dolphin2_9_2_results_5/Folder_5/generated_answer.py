def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    sublist = lst[8:10]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[-2]