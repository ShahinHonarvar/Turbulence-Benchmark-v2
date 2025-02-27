def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = lst[38]
    num2 = lst[52]
    num3 = lst[69]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf