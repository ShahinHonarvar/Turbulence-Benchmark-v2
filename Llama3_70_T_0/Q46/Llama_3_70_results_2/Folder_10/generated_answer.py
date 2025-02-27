def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[86]
    b = lst[89]
    c = lst[49]
    return gcd(gcd(a, b), c)