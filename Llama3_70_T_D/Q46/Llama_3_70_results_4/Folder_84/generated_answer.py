def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (lst[695], lst[710], lst[914])
    return gcd(gcd(a, b), c)