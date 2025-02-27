def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    a = lst[34]
    b = lst[38]
    c = lst[77]
    return gcd(gcd(a, b), c)