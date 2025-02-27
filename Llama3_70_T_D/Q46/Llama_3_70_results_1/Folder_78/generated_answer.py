def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(lst[13], gcd(lst[70], lst[32]))