def gcf_two_nums(lst):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    return gcd(lst[24], lst[68])