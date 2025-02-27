def is_composite(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return True
        i += w
        w = 6 - w
    return False

def composite_nums_between_indices(lst):
    return {num for num in lst[527:539] if is_composite(num)}