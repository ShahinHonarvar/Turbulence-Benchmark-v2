def gcf_three_nums(lst):

    def gcd(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(lst[818], gcd(lst[606], lst[873]))