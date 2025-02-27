def gcf_three_nums(lst):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(lst[9], lst[6]), lst[2])