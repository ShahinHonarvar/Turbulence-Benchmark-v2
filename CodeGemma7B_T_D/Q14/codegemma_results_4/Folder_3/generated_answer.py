def find_second_smallest_num(lst):
    if len(lst) < 29 or not all((isinstance(x, int) for x in lst)):
        return None
    sorted_lst = sorted(lst[27:56])
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]