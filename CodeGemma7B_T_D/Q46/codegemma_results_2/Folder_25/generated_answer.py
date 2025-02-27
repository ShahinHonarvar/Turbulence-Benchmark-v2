def gcf_three_nums(lst):
    a = lst[32]
    b = lst[54]
    c = lst[13]
    gcd = math.gcd(a, b)
    gcd = math.gcd(gcd, c)
    return gcd