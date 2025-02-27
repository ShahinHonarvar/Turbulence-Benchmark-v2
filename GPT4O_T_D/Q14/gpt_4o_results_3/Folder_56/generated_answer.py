def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    sorted_lst = sorted(lst[:2])
    return sorted_lst[1]