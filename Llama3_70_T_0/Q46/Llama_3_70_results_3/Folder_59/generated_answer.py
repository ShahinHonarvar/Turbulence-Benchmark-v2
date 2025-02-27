def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (lst[7], lst[6], lst[8])
    return gcd(gcd(a, b), c)