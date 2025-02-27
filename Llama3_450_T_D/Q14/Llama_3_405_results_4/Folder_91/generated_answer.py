def find_second_smallest_num(lst):
    if len(lst) < 2 or len(lst) > 6:
        return None
    sorted_lst = sorted(lst[:6])
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]