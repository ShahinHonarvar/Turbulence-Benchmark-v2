def find_second_largest_num(lst):
    if len(lst) < 36:
        return None
    sublist = lst[32:36]
    if len(set(sublist)) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1]