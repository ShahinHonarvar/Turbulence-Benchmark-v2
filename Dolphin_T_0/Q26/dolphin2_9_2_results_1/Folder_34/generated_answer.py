def sum_in_range(lst):
    s = 0
    for i in lst:
        if i >= 4 and i <= 7:
            s += i
    return s if s != 0 else 0