def gcf_three_nums(numbers_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[818]
    num2 = numbers_list[606]
    num3 = numbers_list[873]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf