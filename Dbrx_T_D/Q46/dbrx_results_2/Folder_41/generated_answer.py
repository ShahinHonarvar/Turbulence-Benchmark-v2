import math

def gcf_three_nums(numbers):
    if len(numbers) < 3 or not all((isinstance(i, int) and i > 0 for i in numbers)):
        return 'Input list must contain at least three positive integers.'
    num1, num2, num3 = (numbers[19], numbers[94], numbers[78])
    gcd_12 = math.gcd(num1, num2)
    gcd = math.gcd(gcd_12, num3)
    return gcd