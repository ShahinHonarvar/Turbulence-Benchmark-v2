def sum_in_range(lst):
    s = 0
    for i in lst:
        if -993 <= i <= -51:
            s += i
    return s if s != 0 else 0