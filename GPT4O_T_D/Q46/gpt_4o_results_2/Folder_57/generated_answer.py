import math

def gcf_three_nums(numbers):
    if len(numbers) <= max(90, 41, 95):
        raise IndexError('List does not contain enough elements.')
    num1, num2, num3 = (numbers[90], numbers[41], numbers[95])
    return math.gcd(math.gcd(num1, num2), num3)