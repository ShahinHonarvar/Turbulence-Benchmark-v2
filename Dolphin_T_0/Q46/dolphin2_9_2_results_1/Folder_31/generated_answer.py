def gcf_three_nums(lst):
    num1 = lst[90]
    num2 = lst[54]
    num3 = lst[96]

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)

    def gcf_nums(a, b, c):
        res = gcd(a, b)
        return gcd(res, c)
    return gcf_nums(num1, num2, num3)