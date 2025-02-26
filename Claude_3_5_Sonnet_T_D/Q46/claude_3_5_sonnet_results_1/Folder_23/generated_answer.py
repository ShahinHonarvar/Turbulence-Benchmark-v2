def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers[31], numbers[25], numbers[80])
    return gcd(gcd(num1, num2), num3)