def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    a = lst[25]
    b = lst[76]
    c = lst[57]
    return gcd(gcd(a, b), c)