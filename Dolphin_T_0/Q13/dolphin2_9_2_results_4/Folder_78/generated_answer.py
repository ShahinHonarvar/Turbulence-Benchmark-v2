def find_second_largest_num(lst):
    if len(lst) < 52:
        return None
    sublist = lst[43:52]
    if len(set(sublist)) < 2:
        return None
    else:
        sublist.sort()
        return sublist[-2]