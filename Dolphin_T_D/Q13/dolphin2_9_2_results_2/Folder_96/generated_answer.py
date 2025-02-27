def find_second_largest_num(lst):
    sublist = lst[15:52]
    if len(sublist) < 2:
        return None
    first_max = max(sublist)
    sublist.remove(first_max)
    if len(sublist) == 0:
        return None
    second_max = max(sublist)
    return second_max