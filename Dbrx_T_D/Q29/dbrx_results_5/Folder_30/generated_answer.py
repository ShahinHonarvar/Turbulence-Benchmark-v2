from functools import reduce

def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[85]
    num2 = numbers[33]
    return reduce(gcd, filter(lambda x: x > 0, [num1, num2]))