def find_second_largest_num(lst):
    if 8 < len(lst) < 6:
        return None
    sublist = lst[6:9]
    if len(set(sublist)) < 2:
        return None
    else:
        sublist.remove(max(sublist))
        return max(sublist)