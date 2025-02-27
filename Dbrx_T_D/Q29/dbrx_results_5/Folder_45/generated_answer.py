from functools import reduce

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_two_nums(numbers):
    num1 = numbers[47]
    num2 = numbers[97]
    return reduce(gcd, filter(lambda x: x > 0, [num1, num2]))