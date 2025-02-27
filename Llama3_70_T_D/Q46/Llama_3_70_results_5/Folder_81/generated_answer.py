def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[20]
    b = lst[17]
    c = lst[28]
    return gcd(gcd(a, b), c)