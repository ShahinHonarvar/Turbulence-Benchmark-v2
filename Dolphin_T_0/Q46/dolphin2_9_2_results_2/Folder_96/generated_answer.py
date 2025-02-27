def gcf_three_nums(lst):
    a = lst[29]
    b = lst[74]
    c = lst[49]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcd_ab = gcf(a, b)
    gcd_abc = gcf(gcd_ab, c)
    return gcd_abc