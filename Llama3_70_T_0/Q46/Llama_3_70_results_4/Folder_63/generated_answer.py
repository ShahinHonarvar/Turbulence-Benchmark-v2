def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[38]
    b = lst[52]
    c = lst[69]
    return gcd(gcd(a, b), c)