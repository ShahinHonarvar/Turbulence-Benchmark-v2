def gcf_two_nums(l):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(l[37], l[30])