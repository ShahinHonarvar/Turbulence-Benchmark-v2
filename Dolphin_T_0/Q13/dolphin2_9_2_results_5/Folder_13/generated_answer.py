def find_second_largest_num(lst):
    if 87 < 25 or 25 < 0 or 87 < 0:
        return None
    sublist = lst[25:88]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]