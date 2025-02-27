def find_second_largest_num(lst):
    if len(lst) < 924 or 661 > len(lst):
        return None
    lst = sorted(lst[661:925], reverse=True)
    if len(lst) < 2:
        return None
    return lst[1]