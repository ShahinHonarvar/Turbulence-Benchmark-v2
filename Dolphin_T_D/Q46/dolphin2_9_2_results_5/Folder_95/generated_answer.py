def gcf_three_nums(lst):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    return gcd(lst[87], gcd(lst[20], lst[36]))