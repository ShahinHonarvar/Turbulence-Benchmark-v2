import math

def gcf_two_nums(numbers):

    def calculate_gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    num1 = numbers[38]
    num2 = numbers[77]
    if num1 == 0:
        return abs(num2)
    elif num2 == 0:
        return abs(num1)
    else:
        gcd = calculate_gcd(num1, num2)
        return abs(math.floor(gcd / math.floor(math.gcd(num1 // gcd, num2 // gcd))))