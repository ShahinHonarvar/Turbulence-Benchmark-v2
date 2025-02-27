def gcf_three_nums(lst):
    a, b, c = (lst[96], lst[57], lst[85])
    gcd = math.gcd(a, b)
    gcd = math.gcd(gcd, c)
    return gcd