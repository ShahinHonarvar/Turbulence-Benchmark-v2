def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers[21], numbers[51], numbers[33])
    return gcd(gcd(num1, num2), num3)