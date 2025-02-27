import math

def gcf_three_nums(numbers):
    a = numbers[818]
    b = numbers[606]
    c = numbers[873]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return math.gcd(gcd(a, b), c)