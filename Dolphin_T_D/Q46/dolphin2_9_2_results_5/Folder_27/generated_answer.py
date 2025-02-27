def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = lst[76]
    num2 = lst[64]
    num3 = lst[28]
    gcd1n2 = gcd(num1, num2)
    return gcd(gcd1n2, num3)