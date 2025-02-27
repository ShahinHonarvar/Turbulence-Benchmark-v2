def gcf_three_nums(lst):
    num1 = lst[93]
    num2 = lst[94]
    num3 = lst[57]

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(gcd(num1, num2), num3)