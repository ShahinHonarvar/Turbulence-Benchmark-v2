def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[24]
    b = lst[25]
    c = lst[80]
    return gcd(gcd(a, b), c)