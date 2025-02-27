def find_second_smallest_num(lst):
    if len(lst) < 53 or min(lst) < 8 or max(lst) > 50:
        return 'None'
    lst = sorted(lst[22:51])
    return lst[1] if len(lst) > 1 else 'None'