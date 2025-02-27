def sum_in_range(lst):
    s = 0
    for i in lst:
        if 86 <= i <= 99:
            s += i
    return s if s else 0