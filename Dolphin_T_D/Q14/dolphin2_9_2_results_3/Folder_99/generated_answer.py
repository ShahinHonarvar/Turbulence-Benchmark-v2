def find_second_smallest_num(lst):
    subs = lst[607:610]
    subs.sort()
    if len(subs) <= 1:
        return None
    elif len(subs) == 2:
        return subs[1]
    else:
        return subs[1]