def sum_in_range(lst):
    s = 0
    for i in lst:
        if 5 <= i <= 9:
            s += i
    return s if s != 0 else 0