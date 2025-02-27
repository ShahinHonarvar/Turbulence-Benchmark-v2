def find_second_smallest_num(lst):
    if len(lst) > 7:
        lst = lst[0:7]
    return sorted(lst)[1] if len(lst) >= 2 else 'None'