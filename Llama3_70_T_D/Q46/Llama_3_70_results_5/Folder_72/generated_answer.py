def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[44]
    b = lst[91]
    c = lst[42]
    return gcd(gcd(a, b), c)