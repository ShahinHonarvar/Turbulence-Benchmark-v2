def sum_in_range(lst):
    s = 0
    for i in range(len(lst)):
        if lst[i] >= 584 and lst[i] <= 619:
            s += lst[i]
    return s