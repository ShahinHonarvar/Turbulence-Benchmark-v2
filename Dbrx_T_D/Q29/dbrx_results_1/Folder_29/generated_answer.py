import math

def gcf_two_nums(numbers):
    a = numbers[96]
    b = numbers[57]
    return math.gcd(a, b) if a % b == 0 or b % a == 0 else math.gcd(a, b) * (a // math.gcd(a, b)) // (b // math.gcd(a, b))