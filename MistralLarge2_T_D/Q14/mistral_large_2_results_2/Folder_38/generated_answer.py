def find_second_smallest_num(lst):
    sublist = lst[37:52]
    if len(sublist) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for num in sublist:
        if num < min1:
            min2 = min1
            min1 = num
        elif min1 < num < min2:
            min2 = num
    return min2 if min2 != float('inf') else None