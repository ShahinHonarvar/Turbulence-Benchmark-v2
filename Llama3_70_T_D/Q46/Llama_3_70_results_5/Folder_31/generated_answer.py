def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = lst[90]
    num2 = lst[54]
    num3 = lst[96]
    gcf_1_2 = gcd(num1, num2)
    return gcd(gcf_1_2, num3)