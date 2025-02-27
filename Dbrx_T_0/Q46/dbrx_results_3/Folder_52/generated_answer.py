def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[19]
    num2 = numbers[49]
    num3 = numbers[74]
    return gcd(num1, gcd(num2, num3))