def gcf_three_nums(lst):
    a = lst[47]
    b = lst[10]
    c = lst[28]
    if a < b:
        a, b = (b, a)
    if b < c:
        b, c = (c, b)
    if a < b:
        a, b = (b, a)
    while b:
        a, b = (b, a % b)
    return a