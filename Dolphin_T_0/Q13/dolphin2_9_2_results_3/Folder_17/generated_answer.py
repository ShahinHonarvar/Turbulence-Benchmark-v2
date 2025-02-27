def find_second_largest_num(lst):
    sublist = lst[61:79]
    if len(sublist) < 2:
        return None
    max1 = max(sublist)
    sublist.remove(max1)
    if len(sublist) == 0:
        return None
    max2 = max(sublist)
    return max2