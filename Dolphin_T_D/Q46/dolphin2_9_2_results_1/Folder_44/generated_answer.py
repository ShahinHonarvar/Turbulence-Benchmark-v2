def gcf_three_nums(lst):
    num1 = lst[62]
    num2 = lst[96]
    num3 = lst[26]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(num1, num2), num3)