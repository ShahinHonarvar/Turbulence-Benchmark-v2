def find_second_largest_num(lst):
    if len(lst) < 37:
        return None
    sublist = lst[33:37]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]