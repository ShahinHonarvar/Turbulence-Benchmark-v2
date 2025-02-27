def gcf_three_nums(lst):
    num1 = lst[24]
    num2 = lst[45]
    num3 = lst[38]

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    return gcd(gcd(num1, num2), num3)