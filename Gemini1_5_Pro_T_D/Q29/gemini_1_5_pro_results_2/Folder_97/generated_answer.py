def gcf_two_nums(lst):
    a = lst[180]
    b = lst[312]
    while b:
        a, b = (b, a % b)
    return a