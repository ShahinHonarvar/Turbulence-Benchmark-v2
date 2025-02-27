def find_second_largest_num(lst):
    if len(lst) < 10:
        return None
    sublist = lst[8:10]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]