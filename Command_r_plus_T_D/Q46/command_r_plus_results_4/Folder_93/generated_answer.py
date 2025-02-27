def gcf_three_nums(numbers_list):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = numbers_list[25]
    num2 = numbers_list[76]
    num3 = numbers_list[57]
    gcf = gcd(num1, gcd(num2, num3))
    return gcf