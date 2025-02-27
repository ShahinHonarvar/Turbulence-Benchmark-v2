def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[46]
    b = lst[84]
    c = lst[23]
    return gcd(gcd(a, b), c)