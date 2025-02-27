def gcf_three_nums(lst):
    num1 = lst[66]
    num2 = lst[56]
    num3 = lst[92]

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def gcf(a, b, c):
        gcd_ab = gcd(a, b)
        return gcd(gcd_ab, c)
    return gcf(num1, num2, num3)