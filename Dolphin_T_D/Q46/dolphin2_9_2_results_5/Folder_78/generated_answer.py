def gcf_three_nums(lst):
    a = lst[13]
    b = lst[70]
    c = lst[32]
    if a < b:
        a, b = (b, a)
    if b < c:
        b, c = (c, b)
    if a < b:
        a, b = (b, a)
    while b % a != 0:
        a, b = (b % a, a)
    return a