def find_second_smallest_num(lst):
    lst = sorted(lst[22:64])
    if len(lst) < 2:
        return None
    else:
        return lst[1]