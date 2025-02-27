def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    elif len(lst) == 2:
        return min(lst)
    else:
        max_num = max(lst[25:88])
        lst.remove(max_num)
        second_max_num = max(lst[25:88])
        return second_max_num if second_max_num != max_num else None