def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(lst[47], lst[10])
    gcf = gcd(gcf, lst[28])
    return gcf