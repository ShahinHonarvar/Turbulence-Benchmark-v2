import math

def gcf_three_nums(numbers):
    num1 = numbers[44]
    num2 = numbers[91]
    num3 = numbers[42]

    def gcd(a, b):
        return math.gcd(a, b)

    def lcm(a, b):
        return a * b // math.gcd(a, b)

    def find_gcd(element1, element2):
        gcd_val = gcd(element1, element2)
        lcm_val = lcm(element1, element2)
        return gcd(lcm_val, gcd_val)
    return find_gcd(num1, num2) if num1 == num2 else find_gcd(find_gcd(num1, num2), num3)