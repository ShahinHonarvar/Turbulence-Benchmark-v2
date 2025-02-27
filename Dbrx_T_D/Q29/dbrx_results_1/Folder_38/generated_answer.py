import math

def gcf_two_nums(numbers):
    num1, num2 = (numbers[88], numbers[35])
    factor = math.gcd(num1, num2)
    while factor > 1:
        factor -= 1
        if num1 % factor == 0 and num2 % factor == 0:
            break
    return factor