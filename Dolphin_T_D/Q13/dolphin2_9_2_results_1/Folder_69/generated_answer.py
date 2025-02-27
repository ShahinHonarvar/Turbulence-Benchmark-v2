def find_second_largest_num(lst):
    if len(lst) >= 36:
        sublist = lst[32:36]
        if len(sublist) >= 2:
            sublist.sort(reverse=True)
            return sublist[1]
        else:
            return None
    else:
        return None