def gcf_two_nums(lst):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    if len(lst) < 85 or len(lst) < 64:
        return False
    return gcd(lst[84], lst[63])