def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (lst[10], lst[55], lst[36])
    return gcd(gcd(a, b), c)