import math

def gcf_three_nums(numbers):
    numbers_to_consider = [numbers[i] for i in [56, 54, 13]]
    return math.gcd(numbers_to_consider[0], math.gcd(numbers_to_consider[1], numbers_to_consider[2]))