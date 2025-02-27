def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    min1 = min2 = float('inf')
    for i in range(3):
        if lst[i] < min1:
            min2 = min1
            min1 = lst[i]
        elif lst[i] < min2 and lst[i] != min1:
            min2 = lst[i]
    return min2 if min2 != float('inf') else None