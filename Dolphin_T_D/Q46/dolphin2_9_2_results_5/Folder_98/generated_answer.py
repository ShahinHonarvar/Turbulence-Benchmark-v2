def gcf_three_nums(lst):
    a = lst[8]
    b = lst[2]
    c = lst[1]
    if a < b:
        a, b = (b, a)
    if b < c:
        b, c = (c, b)
    if a < b:
        a, b = (b, a)
    while a % b == 0:
        a, b = (b, a % b)
    return b