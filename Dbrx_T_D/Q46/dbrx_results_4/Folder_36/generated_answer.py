import math

def gcf_three_nums(numbers):
    a = numbers[427]
    b = numbers[761]
    c = numbers[148]

    def gcd(a, b):
        return math.gcd(a, b)
    first_gcd = gcd(a, b)
    return gcd(first_gcd, c)