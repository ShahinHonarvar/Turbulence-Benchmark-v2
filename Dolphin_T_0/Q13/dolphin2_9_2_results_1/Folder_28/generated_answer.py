def find_second_largest_num(lst):
    sublist = lst[62:64]
    if len(sublist) == 0:
        return None
    if len(set(sublist)) == 1:
        return None
    first_max = max(sublist)
    sublist.remove(first_max)
    return max(sublist)