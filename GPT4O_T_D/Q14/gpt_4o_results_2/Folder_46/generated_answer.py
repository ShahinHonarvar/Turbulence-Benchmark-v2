def find_second_smallest_num(lst):
    sub_lst = lst[13:69]
    if len(sub_lst) < 2:
        return None
    unique_sorted = sorted(set(sub_lst))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]