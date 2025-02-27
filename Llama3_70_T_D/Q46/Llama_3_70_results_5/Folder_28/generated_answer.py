def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(lst[99], lst[63])
    gcf = gcd(gcf, lst[74])
    return gcf