def find_second_largest_num(lst):
    if len(lst) <= 51:
        return None
    sublist = lst[29:52]
    if len(sublist) < 2:
        return None
    first_largest = max(sublist)
    sublist.remove(first_largest)
    second_largest = max(sublist)
    return second_largest