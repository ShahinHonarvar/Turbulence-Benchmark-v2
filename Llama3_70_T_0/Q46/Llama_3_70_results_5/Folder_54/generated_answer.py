def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[96]
    b = lst[57]
    c = lst[85]
    return gcd(gcd(a, b), c)