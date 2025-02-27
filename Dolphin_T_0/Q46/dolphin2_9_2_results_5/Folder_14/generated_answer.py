def gcf_three_nums(lst):
    n1 = lst[17]
    n2 = lst[88]
    n3 = lst[35]

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    gcf = gcd(n1, n2)
    gcf = gcd(gcf, n3)
    return gcf