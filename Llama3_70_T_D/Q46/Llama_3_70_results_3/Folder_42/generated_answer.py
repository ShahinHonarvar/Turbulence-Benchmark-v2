def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[19]
    b = lst[69]
    c = lst[97]
    return gcd(gcd(a, b), c)