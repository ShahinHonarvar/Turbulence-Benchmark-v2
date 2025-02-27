def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(lst[742], lst[888])
    gcf = gcd(gcf, lst[629])
    return gcf