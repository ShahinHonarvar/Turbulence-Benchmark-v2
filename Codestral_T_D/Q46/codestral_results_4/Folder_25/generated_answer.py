def gcf_three_nums(lst):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = lst[32]
    num2 = lst[54]
    num3 = lst[13]
    return gcd(gcd(num1, num2), num3)