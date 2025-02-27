from fractions import gcd

def gcf_three_nums(numbers):
    nums = [numbers[742], numbers[888], numbers[629]]
    return reduce(gcd, nums)