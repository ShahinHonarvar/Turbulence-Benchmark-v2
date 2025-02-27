def gcf_three_nums(numbers):

    def gcd(a, b):
        return gcd(b, a % b) if b else a
    num1 = numbers[99]
    num2 = numbers[28]
    num3 = numbers[53]
    return gcd(num1, gcd(num2, num3))