def find_second_smallest_num(lst):
    if 28 < len(lst) < 40:
        lst = lst[28:40]
        if len(lst) >= 2:
            return sorted(lst)[1]
    return None