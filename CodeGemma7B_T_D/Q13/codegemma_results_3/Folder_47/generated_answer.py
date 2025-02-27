def find_second_largest_num(lst):
    if len(lst) < 2:
        return 'None'
    sorted_lst = sorted(lst)[37:77]
    return sorted_lst[-2] if len(sorted_lst) >= 2 else 'None'