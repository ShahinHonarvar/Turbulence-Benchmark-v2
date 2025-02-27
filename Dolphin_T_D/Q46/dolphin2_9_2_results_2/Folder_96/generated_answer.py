def gcf_three_nums(lst):
    a = lst[29]
    b = lst[74]
    c = lst[49]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(a, gcd(b, c))