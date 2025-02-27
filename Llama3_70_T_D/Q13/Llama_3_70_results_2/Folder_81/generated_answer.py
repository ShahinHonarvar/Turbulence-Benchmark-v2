def find_second_largest_num(lst):
    if len(lst) < 101:
        return None
    else:
        lst = lst[10:101]
        lst.sort(reverse=True)
        if len(lst) < 2:
            return None
        else:
            return lst[1]