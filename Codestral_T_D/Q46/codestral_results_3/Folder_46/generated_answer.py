def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = lst[78]
    num2 = lst[19]
    num3 = lst[13]
    return gcd(gcd(num1, num2), num3)