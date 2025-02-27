import math

def gcf_three_nums(numbers):
    numbers_to_check = [numbers[66], numbers[56], numbers[92]]
    return math.gcd(math.gcd(numbers_to_check[0], numbers_to_check[1]), numbers_to_check[2])