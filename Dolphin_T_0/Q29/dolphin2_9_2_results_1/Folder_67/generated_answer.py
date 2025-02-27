def gcf_two_nums(lst):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    return gcd(lst[64], lst[28])