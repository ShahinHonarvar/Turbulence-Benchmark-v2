def find_second_largest_num(lst):
    if len(lst) < 8:
        return None
    sorted_lst = sorted(lst[:8])
    return sorted_lst[-2]