def gcf_three_nums(lst):
    a = lst[90]
    b = lst[41]
    c = lst[95]

    def gcd(a, b):
        while b > 0:
            a, b = (b, a % b)
        return a

    def gcf(a, b, c):
        return gcd(a, gcd(b, c))
    return gcf(a, b, c)