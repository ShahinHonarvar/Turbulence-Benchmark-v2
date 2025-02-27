import math

def gcf_three_nums(numbers):

    def gcf(a, b):
        return math.gcd(a, b)
    return gcf(gcf(numbers[695], numbers[710]), numbers[914])