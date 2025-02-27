def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[19]
    b = lst[94]
    c = lst[78]
    result = gcd(a, gcd(b, c))
    return result