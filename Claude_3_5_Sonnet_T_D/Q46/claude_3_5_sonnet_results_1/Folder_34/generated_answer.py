def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 54:
        return None
    num1 = numbers[53]
    num2 = numbers[23]
    num3 = numbers[45]
    return gcd(gcd(num1, num2), num3)