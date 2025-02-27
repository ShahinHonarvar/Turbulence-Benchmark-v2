def find_second_largest_num(lst):
    sub = lst[8:10]
    if len(sub) != 2:
        return None
    else:
        return sorted(sub)[-2]