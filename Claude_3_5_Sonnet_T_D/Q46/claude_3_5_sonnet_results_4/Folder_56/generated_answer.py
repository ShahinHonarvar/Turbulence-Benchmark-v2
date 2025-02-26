from math import gcd
    from functools import reduce

def gcf_three_nums(numbers):
    indices = [59, 93, 84]
    selected_nums = [numbers[i] for i in indices if i < len(numbers)]
    if len(selected_nums) < 3:
        return None
    return reduce(gcd, selected_nums)