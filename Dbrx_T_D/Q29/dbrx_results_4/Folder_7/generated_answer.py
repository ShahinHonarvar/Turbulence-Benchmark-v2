import math

def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[224]
    num2 = numbers[663]
    return int(math.sqrt(num1 * num2) * gcd(num1, num2))