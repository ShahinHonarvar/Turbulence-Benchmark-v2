import math

def gcf_three_nums(numbers):
    a = numbers[558]
    b = numbers[110]
    c = numbers[628]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    common_factor = lcm(a, b)
    return gcd(common_factor, c)