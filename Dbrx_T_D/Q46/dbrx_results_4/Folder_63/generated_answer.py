from functools import reduce

def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    nums_at_indices = [numbers[i] for i in [38, 52, 69]]
    return reduce(gcd, nums_at_indices)