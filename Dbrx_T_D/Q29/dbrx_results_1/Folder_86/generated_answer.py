from math import gcd

def get_nums_from_indices(lst, indices):
    return [lst[i] for i in indices if 0 <= i < len(lst)]

def gcf_two_nums(lst):
    nums = get_nums_from_indices(lst, [793, 449])
    return reduce(gcd, nums) if nums else 0