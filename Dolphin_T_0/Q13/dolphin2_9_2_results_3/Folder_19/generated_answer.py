def find_second_largest_num(lst):
    sublist = lst[3:6]
    if len(sublist) < 2:
        return None
    else:
        max1 = max(sublist)
        sublist.remove(max1)
        if len(sublist) == 0:
            return None
        else:
            max2 = max(sublist)
            return max2