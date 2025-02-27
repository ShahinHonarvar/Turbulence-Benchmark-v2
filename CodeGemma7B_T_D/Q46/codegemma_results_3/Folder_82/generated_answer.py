def gcf_three_nums(l):
    n1, n2, n3 = (l[67], l[84], l[13])
    if n2 > n1:
        n1, n2 = (n2, n1)
    if n3 > n1:
        n1, n3 = (n3, n1)
    if n3 > n2:
        n2, n3 = (n3, n2)
    while n2 != 0:
        n1, n2 = (n2, n1 % n2)
    return n1