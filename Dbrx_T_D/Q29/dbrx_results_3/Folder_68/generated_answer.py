from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) < 2:
        return 'Error: List must contain at least two numbers.'
    num1, num2 = (numbers[8], numbers[9])
    if num1 <= 0 or num2 <= 0:
        return 'Error: Both numbers must be positive.'
    return gcd(num1, num2)