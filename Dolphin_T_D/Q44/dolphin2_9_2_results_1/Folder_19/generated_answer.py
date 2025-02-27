import math

def is_composite(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(5, 8):
        if is_composite(lst[i]):
            composite_nums.add(lst[i])
    return composite_nums