def gcf_three_nums(lst):
    a = lst[637]
    b = lst[411]
    c = lst[757]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(a, b), c)