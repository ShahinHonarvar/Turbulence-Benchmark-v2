def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(lst[654], gcd(lst[312], lst[441]))