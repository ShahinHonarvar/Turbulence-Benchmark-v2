def sum_in_range(lst):
    s = 0
    for i in lst:
        if 3 <= i <= 6:
            s += i
    return s