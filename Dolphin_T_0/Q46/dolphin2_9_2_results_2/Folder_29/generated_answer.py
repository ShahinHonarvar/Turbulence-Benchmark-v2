def gcf_three_nums(lst):

    def gcf(a, b):
        while b > 0:
            a, b = (b, a % b)
        return a
    gcd = gcf(lst[22], lst[97])
    gcd = gcf(gcd, lst[64])
    return gcd