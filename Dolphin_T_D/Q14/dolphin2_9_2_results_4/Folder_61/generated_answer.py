def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for i in range(8):
        if lst[i] < min1:
            min1, min2 = (lst[i], min1)
        elif lst[i] < min2 and lst[i] != min1:
            min2 = lst[i]
    return min2 if min2 != float('inf') else None