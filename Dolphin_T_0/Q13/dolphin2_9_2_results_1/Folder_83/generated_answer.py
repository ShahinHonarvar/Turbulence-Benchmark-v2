def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    elif len(lst) == 2:
        return None
    else:
        max_num = max(lst[90:91])
        second_max_num = None
        for i in lst[90:91]:
            if i != max_num:
                second_max_num = i
                break
        return second_max_num if second_max_num else None