def gcf_three_nums(numbers):
    num1 = numbers[20]
    num2 = numbers[17]
    num3 = numbers[28]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(num1, num2), num3)