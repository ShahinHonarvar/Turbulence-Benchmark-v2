import math

def gcf_three_nums(numbers):
    a, b, c = (numbers[912], numbers[170], numbers[500])
    return math.gcd(math.gcd(a, b), c)