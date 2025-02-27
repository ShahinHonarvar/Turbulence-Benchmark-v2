def gcf_two_nums(lst):

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    return gcd(lst[360], lst[722])