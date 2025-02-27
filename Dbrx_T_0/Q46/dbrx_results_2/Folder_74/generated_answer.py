def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers[99], numbers[95], numbers[80])
    return gcd(num1, gcd(num2, num3))