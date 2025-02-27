def find_second_smallest_num(lst):
    if not lst:
        return None
    min_1 = min(lst[59:98])
    if min_1 == len(lst[59:98]):
        return None
    del lst[lst.index(min_1) + 59]
    if len(lst[59:98]) < 1:
        return None
    min_2 = min(lst[59:98])
    return min_2 if min_2 != min_1 else None