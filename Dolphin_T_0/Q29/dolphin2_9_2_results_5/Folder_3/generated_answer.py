def gcf_two_nums(lst):
    a = lst[47]
    b = lst[10]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(a, b)