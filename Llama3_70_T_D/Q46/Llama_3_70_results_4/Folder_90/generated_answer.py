def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[818]
    b = lst[606]
    c = lst[873]
    g = gcd(a, b)
    return gcd(g, c)