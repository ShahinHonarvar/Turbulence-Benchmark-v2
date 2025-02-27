def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(lst[24], lst[25])
    return gcd(gcf, lst[80])