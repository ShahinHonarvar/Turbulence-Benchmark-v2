def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (lst[66], lst[90], lst[27])
    return gcd(gcd(a, b), c)