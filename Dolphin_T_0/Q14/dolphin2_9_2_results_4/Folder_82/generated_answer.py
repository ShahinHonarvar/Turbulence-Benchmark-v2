def find_second_smallest_num(lst):
    if len(lst) < 20:
        return None
    elif len(lst) > 200:
        lst = lst[20:201]
    else:
        lst = lst[20:]
    if len(lst) < 2 or len(set(lst)) < 2:
        return None
    min_1 = min(lst)
    min_2 = min((x for x in lst if x != min_1))
    return min_2 if min_2 < float('inf') else None