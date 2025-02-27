def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = lst[93]
    num2 = lst[94]
    num3 = lst[57]
    return gcd(gcd(num1, num2), num3)