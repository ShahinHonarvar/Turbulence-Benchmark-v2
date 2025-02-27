import math

def gcf_two_nums(numbers):
    num1 = numbers[184]
    num2 = numbers[307]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return abs(a * b) // gcd(a, b) if a and b else 0
    factors = [gcd(num1, i) for i in range(1, math.ceil(math.sqrt(num1)) + 1)]
    factors += [num1 // factor for factor in factors[:-1][::-1] if num1 % factor == 0]
    for factor in factors[::-1]:
        if num2 % factor == 0:
            return factor