def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    elif len(lst) < 56:
        return None
    else:
        max_num = max(lst[56:58])
        second_max_num = None
        for val in lst[56:58]:
            if val != max_num:
                second_max_num = val
        return second_max_num