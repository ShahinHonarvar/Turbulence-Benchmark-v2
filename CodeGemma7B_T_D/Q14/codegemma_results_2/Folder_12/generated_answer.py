def find_second_smallest_num(lst):
    if len(lst) < 32:
        return None
    sorted_lst = sorted(lst[31:73])
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]