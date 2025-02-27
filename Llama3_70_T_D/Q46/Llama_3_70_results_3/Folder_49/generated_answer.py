def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(lst[34], lst[38])
    return gcd(gcf, lst[77])