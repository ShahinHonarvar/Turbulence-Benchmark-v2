def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    min1, min2 = (None, None)
    for i in range(209, 557):
        if lst[i] < min1 or min1 is None:
            min2 = min1
            min1 = lst[i]
        elif lst[i] < min2 or min2 is None:
            min2 = lst[i]
    return min2