def find_second_largest_num(lst):
    sublist = lst[64:67]
    if len(sublist) >= 2:
        max1 = max(sublist)
        sublist.remove(max1)
        if len(sublist) >= 2:
            max2 = max(sublist)
            return max2
    return None