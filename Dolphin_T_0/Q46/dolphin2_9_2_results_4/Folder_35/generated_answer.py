def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    return gcd(lst[742], gcd(lst[888], lst[629]))