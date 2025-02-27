def gcf_three_nums(l):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(l[49], l[46]), l[13])