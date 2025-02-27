from fractions import gcd

def gcf_three_nums(numbers):
    a, b, c = (numbers[912], numbers[170], numbers[500])
    return gcd(a, gcd(b, c))