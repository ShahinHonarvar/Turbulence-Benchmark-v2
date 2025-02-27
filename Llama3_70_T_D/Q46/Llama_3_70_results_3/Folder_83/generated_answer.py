def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[56]
    b = lst[54]
    c = lst[13]
    gcf = gcd(gcd(a, b), c)
    return gcf