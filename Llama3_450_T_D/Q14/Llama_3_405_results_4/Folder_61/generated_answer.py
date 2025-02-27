def find_second_smallest_num(lst):
    if len(lst) < 2 or 8 < len(lst):
        return None
    sorted_lst = sorted(lst)
    return sorted_lst[1]