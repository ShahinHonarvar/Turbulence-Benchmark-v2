def sum_in_range(lst):
    s = 0
    for i in range(-10, 49):
        if i in lst:
            s += i
    return s