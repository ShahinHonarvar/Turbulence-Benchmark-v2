import functools

def gcf_three_nums(numbers):
    nums_at_indices = [numbers[307], numbers[920], numbers[463]]
    gcf = functools.reduce(gcd, nums_at_indices)
    return gcf

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a