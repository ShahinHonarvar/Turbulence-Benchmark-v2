def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = lst[818]
    num2 = lst[606]
    num3 = lst[873]
    result = gcd(num1, num2)
    result = gcd(result, num3)
    return result