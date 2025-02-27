def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = lst[252]
    num2 = lst[149]
    num3 = lst[564]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf