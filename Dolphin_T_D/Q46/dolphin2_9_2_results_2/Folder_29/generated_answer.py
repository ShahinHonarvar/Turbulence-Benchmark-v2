def gcf_three_nums(lst):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    num1 = lst[22]
    num2 = lst[97]
    num3 = lst[64]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf