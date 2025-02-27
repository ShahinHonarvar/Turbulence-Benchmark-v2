def gcf_three_nums(numbers):

    def gcd(x, y):
        while x % y != 0:
            x, y = (y, x % y)
        return y
    num1 = numbers[31]
    num2 = numbers[25]
    num3 = numbers[80]
    gcf = gcd(num1, gcd(num2, num3))
    return gcf