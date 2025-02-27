def gcf_two_nums(lst):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(lst[54], lst[13])