def find_second_smallest_num(lst):
    lst = lst[20:201]
    if len(lst) == 0:
        return None
    else:
        return sorted(lst)[1]