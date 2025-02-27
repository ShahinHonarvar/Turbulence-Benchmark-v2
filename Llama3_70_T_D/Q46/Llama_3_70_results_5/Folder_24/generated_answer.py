def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (lst[18], lst[37], lst[43])
    return gcd(gcd(a, b), c)