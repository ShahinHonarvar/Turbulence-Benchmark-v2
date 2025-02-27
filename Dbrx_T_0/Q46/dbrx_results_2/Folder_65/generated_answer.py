def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[18]
    num2 = numbers[10]
    num3 = numbers[76]
    return gcd(num1, gcd(num2, num3))