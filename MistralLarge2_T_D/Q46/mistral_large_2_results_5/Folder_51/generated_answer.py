def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = lst[21]
    num2 = lst[69]
    num3 = lst[41]
    return gcd(gcd(num1, num2), num3)