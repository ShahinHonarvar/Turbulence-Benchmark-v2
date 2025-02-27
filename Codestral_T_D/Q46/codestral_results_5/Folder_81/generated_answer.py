def gcf_three_nums(lst):
    num1 = lst[20]
    num2 = lst[17]
    num3 = lst[28]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(num1, num2), num3)