def gcf_three_nums(lst):
    num1 = lst[8]
    num2 = lst[9]
    num3 = lst[3]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(num1, gcd(num2, num3))
    return gcf