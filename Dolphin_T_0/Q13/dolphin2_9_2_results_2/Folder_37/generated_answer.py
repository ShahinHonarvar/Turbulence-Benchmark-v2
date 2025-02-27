def find_second_largest_num(lst):
    if len(lst) == 0:
        return None
    elif len(lst) < 5:
        return None
    else:
        sublist = lst[1:6]
        max_num = max(sublist)
        sublist.remove(max_num)
        if len(sublist) == 0:
            return None
        else:
            return max(sublist)