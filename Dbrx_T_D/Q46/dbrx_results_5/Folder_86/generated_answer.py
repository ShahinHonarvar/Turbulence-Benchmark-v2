def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[340]
    num2 = numbers[237]
    num3 = numbers[373]
    return gcd(num1, gcd(num2, num3))