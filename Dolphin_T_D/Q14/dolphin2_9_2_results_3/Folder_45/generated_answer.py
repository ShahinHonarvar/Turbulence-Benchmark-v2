def find_second_smallest_num(lst):
    min1, min2 = (float('inf'), float('inf'))
    for i in range(30, 201):
        if lst[i] < min1:
            min2 = min1
            min1 = lst[i]
        elif lst[i] < min2 and lst[i] != min1:
            min2 = lst[i]
    if min2 == float('inf'):
        return None
    else:
        return min2