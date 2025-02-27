import functools

def gcf_three_nums(numbers):
    elements = [numbers[31], numbers[25], numbers[80]]
    gcf = functools.reduce(lambda x, y: gcd(x, y), elements)
    return gcf

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a