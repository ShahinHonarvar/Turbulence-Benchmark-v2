def find_second_smallest_num(lst):
    if len(lst) < 200:
        return None
    lst = lst[49:201]
    if len(lst) < 2:
        return None
    min1, min2 = (min(lst[0:2]), max(lst[0:2]))
    for i in range(2, len(lst)):
        if lst[i] < min1:
            min1, min2 = (lst[i], min1)
        elif min1 < lst[i] < min2:
            min2 = lst[i]
    return min2 if min2 != max(lst[0:2]) else None