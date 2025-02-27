def gcf_two_nums(lst):
    n1 = lst[42]
    n2 = lst[25]
    a, b = (min(n1, n2), max(n1, n2))
    while a:
        a, b = (b % a, a)
    return a