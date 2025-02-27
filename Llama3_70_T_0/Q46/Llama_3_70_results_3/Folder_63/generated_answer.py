def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(lst[38], lst[52]), lst[69])