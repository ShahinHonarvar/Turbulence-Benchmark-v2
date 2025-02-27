def find_second_largest_num(lst):
    if 78 < len(lst) < 62:
        return None
    else:
        sublist = lst[62:79]
        sublist.sort(reverse=True)
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]