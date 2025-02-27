def gcf_three_nums(l):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(l[37], l[30]), l[48])