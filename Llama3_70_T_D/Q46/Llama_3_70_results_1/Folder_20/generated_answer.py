def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = lst[29]
    gcf = gcd(gcf, lst[53])
    gcf = gcd(gcf, lst[42])
    return gcf