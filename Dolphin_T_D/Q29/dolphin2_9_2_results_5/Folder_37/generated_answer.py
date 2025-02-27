def gcf_two_nums(lst):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(lst[29], lst[74])