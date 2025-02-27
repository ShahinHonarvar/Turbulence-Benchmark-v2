import functools

def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    nums_at_indices = [numbers[14], numbers[21], numbers[17]]
    return functools.reduce(gcd, nums_at_indices)