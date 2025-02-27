def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers[427], numbers[761], numbers[148])
    return gcd(gcd(num1, num2), num3)