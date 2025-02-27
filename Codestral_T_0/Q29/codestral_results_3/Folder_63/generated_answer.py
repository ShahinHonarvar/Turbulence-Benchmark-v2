def gcf_two_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(lst[21], lst[17])