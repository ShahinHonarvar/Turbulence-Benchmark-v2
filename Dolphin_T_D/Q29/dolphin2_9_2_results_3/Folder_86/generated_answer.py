def gcf_two_nums(l):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    return gcd(l[793], l[449])