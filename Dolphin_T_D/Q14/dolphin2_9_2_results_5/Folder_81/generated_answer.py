def find_second_smallest_num(lst):
    sublist = lst[10:101]
    if len(sublist) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for sub in sublist:
        if sub < min1:
            min1, min2 = (sub, min1)
        elif min1 < sub < min2:
            min2 = sub
    return min2 if min2 < float('inf') else None