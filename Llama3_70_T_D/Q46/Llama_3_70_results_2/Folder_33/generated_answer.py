def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (lst[252], lst[149], lst[564])
    gcf_ab = gcd(a, b)
    return gcd(gcf_ab, c)