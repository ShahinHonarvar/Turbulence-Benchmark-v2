def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(lst[90], lst[54]), lst[96])