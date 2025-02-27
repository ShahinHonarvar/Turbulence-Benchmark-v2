def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    min1, min2 = (lst[0], None)
    for i in range(1, len(lst)):
        if lst[i] < min1:
            min2, min1 = (min1, lst[i])
        elif min2 == None or (lst[i] < min2 and lst[i] != min1):
            min2 = lst[i]
    return min2