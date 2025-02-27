def gcf_three_nums(numbers_list):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = numbers_list[91]
    num2 = numbers_list[45]
    num3 = numbers_list[48]
    gcf = gcd(gcd(num1, num2), num3)
    return gcf