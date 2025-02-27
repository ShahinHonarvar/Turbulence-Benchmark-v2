def gcf_three_nums(lst):
    a = lst[56]
    b = lst[54]
    c = lst[13]
    if a < b:
        a, b = (b, a)
    if b < c:
        b, c = (c, b)
    if a < b:
        a, b = (b, a)
    while b != 0:
        a, b = (b, a % b)
    return a