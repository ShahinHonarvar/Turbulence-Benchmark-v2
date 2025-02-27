def gcf_three_nums(numbers):

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return abs(x)
    number1 = numbers[70]
    number2 = numbers[41]
    number3 = numbers[20]
    return gcd(number1, gcd(number2, number3))