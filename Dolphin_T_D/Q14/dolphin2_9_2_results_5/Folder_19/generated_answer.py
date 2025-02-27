def find_second_smallest_num(lst):
    if len(lst) < 5 or len(lst) > 8 or len(lst) != len(set(lst)):
        return None
    small, small2 = (None, None)
    for x in lst[4:9]:
        if small is None or x < small:
            small2 = small
            small = x
        elif small2 is None or x < small2:
            small2 = x
    return small2