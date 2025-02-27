def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[36]
    b = lst[85]
    c = lst[83]
    return gcd(gcd(a, b), c)