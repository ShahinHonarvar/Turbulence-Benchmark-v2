from collections import gcd

def gcf_three_nums(numbers):
    return gcd(numbers[63], gcd(numbers[73], numbers[11]))