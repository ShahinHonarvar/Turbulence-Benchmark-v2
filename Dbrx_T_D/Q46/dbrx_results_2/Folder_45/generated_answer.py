import math

def gcf_three_nums(numbers: list[int]) -> int:
    num1, num2, num3 = (numbers[46 - 1], numbers[84 - 1], numbers[23 - 1])
    factor = math.gcd(num1, num2)
    return math.gcd(factor, num3)