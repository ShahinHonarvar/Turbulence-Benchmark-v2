def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 71:
        return None
    num1, num2, num3 = (numbers[13], numbers[70], numbers[32])
    return gcd(gcd(num1, num2), num3)