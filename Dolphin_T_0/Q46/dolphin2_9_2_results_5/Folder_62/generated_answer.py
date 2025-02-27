def gcf_three_nums(lst):
    a = lst[10]
    b = lst[55]
    c = lst[36]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcd_ab = gcd(a, b)
    gcd_abc = gcd(gcd_ab, c)
    return gcd_abc