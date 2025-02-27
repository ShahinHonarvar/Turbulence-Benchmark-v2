def find_second_largest_num(lst):
    sublist = lst[30:49]
    if not sublist:
        return None
    else:
        max_num = max(sublist)
        sublist.remove(max_num)
        if not sublist:
            return None
        else:
            return max(sublist)