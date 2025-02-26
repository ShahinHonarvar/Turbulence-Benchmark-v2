def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 71:
        return None
    num1 = numbers[70]
    num2 = numbers[41]
    num3 = numbers[20]
    return gcd(gcd(num1, num2), num3)