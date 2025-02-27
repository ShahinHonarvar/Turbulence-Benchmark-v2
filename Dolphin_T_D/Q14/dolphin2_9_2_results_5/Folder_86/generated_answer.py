def find_second_smallest_num(lst):
    sub = lst[33:37]
    if len(sub) < 2:
        return None
    sub.sort()
    return sub[1]