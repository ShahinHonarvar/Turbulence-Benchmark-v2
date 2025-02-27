def find_second_largest_num(lst):
    lst = sorted(lst[64:67], reverse=True)
    if len(lst) < 2:
        return None
    return lst[1]