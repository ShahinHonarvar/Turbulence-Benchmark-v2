def gcf_two_nums(lst):
    a = lst[36]
    b = lst[85]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(a, b)