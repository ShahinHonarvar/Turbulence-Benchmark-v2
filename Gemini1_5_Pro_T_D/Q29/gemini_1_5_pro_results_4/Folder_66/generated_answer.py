def gcf_two_nums(lst):
    a = lst[86]
    b = lst[89]
    while b:
        a, b = (b, a % b)
    return a