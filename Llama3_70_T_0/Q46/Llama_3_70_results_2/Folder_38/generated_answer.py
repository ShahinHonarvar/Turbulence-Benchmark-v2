def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[14]
    b = lst[21]
    c = lst[17]
    return gcd(gcd(a, b), c)