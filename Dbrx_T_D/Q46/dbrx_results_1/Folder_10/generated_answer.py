import math

def gcf_three_nums(numbers):
    num_list = [numbers[86], numbers[89], numbers[49]]

    def gcd(a, b):
        return math.gcd(a, b) if b else abs(a)
    return abs(reduce(gcd, num_list))