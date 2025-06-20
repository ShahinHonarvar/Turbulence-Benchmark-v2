def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[29]
    num2 = numbers[53]
    num3 = numbers[42]
    return gcd(gcd(num1, num2), num3)