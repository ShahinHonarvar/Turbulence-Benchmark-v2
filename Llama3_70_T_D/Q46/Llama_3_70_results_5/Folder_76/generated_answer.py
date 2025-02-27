def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(gcd(lst[876], lst[203]), lst[100])
    return gcf