def gcf_two_nums(lst):
    a = lst[41]
    b = lst[69]
    while b:
        a, b = (b, a % b)
    return a