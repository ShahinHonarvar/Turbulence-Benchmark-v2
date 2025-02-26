def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 93:
        return None
    num1, num2, num3 = (numbers[66], numbers[56], numbers[92])
    return gcd(gcd(num1, num2), num3)