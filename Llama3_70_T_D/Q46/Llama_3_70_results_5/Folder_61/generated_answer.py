def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (lst[1], lst[2], lst[7])
    return gcd(gcd(num1, num2), num3)