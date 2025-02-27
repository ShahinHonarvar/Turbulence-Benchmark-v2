def sum_in_range(lst):
    s = 0
    for i in lst:
        if 1 <= i <= 7:
            s += i
    if s == 0:
        return 0
    return s