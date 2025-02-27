def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[31]
    b = lst[69]
    c = lst[40]
    return gcd(gcd(a, b), c)