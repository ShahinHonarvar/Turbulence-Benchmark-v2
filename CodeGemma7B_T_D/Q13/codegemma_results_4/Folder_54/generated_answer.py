def find_second_largest_num(lst):
    if len(lst) <= 33:
        return 'None'
    sorted_lst = sorted(lst[34:56])[::-1]
    if len(sorted_lst) == 1:
        return 'None'
    return sorted_lst[1]