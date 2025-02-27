import math

def is_composite(n):
    if n <= 1:
        return False
    sqrt_n = math.sqrt(n)
    for i in range(2, int(sqrt_n) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    return {n for n in lst[66:94] if is_composite(n)}