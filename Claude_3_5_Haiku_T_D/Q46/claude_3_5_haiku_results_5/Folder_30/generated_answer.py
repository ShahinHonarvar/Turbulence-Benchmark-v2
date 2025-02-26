def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_multiple(a, b, c):
        return gcd(gcd(a, b), c)
    return gcd_multiple(lst[76], lst[35], lst[74])