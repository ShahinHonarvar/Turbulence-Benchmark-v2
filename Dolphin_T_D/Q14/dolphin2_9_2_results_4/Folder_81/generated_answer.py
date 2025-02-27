def find_second_smallest_num(lst):
    if 10 <= len(lst) <= 100:
        lst = sorted(lst[10:101])
        if len(lst) > 1:
            return lst[1]
    return None