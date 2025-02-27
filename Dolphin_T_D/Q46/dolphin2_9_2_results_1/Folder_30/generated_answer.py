def gcf_three_nums(lst):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    num1 = lst[76]
    num2 = lst[35]
    num3 = lst[74]
    return gcd(gcd(num1, num2), num3)