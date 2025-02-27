def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    min1 = min(lst[:2])
    min2 = max(lst[:2])
    for i in range(2, len(lst)):
        if lst[i] != min1:
            if lst[i] < min1:
                min2 = min1
                min1 = lst[i]
            elif lst[i] < min2:
                min2 = lst[i]
    return min2 if min2 != max(lst[:2]) else None