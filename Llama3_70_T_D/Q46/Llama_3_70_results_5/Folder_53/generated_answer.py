def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(lst[66], lst[56])
    return gcd(gcf, lst[92])