def find_second_largest_num(lst):
    if 36 < len(lst) < 77:
        lst = lst[36:77]
        if len(lst) < 2:
            return None
        else:
            lst.sort()
            return lst[-2]
    else:
        return None