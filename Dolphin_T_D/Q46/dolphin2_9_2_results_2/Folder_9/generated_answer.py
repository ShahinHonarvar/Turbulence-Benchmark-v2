def gcf_three_nums(lst):
    num1 = lst[66]
    num2 = lst[90]
    num3 = lst[27]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf