from itertools import filter false, islice

def composite_nums_between_indices(nums):
    return {x for x in islice(filter(is_composite, nums), 78 - 17 + 1) if x in range(17, 79)}

def is_composite(num):
    return not all((num % i for i in range(2, int(num ** 0.5) + 1)))