import math

def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    return {i for i in lst if is_composite(i)}