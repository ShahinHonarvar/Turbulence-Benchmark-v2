def gcf_three_nums(lst):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(lst[90], gcd(lst[41], lst[95]))