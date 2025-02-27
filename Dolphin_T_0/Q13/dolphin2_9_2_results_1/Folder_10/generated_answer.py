def find_second_largest_num(lst):
    sublist = lst[25:60]
    if len(sublist) < 2:
        return None
    else:
        max_num = max(sublist)
        sublist.remove(max_num)
        if len(sublist) == 0:
            return None
        else:
            return max(sublist)