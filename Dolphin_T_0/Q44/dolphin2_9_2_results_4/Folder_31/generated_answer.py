def is_composite(n):
    if n <= 1:
        return False
    elif n <= 3:
        return False
    elif n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False

def composite_nums_between_indices(lst):
    return {n for i, n in enumerate(lst) if i >= 56 and i <= 66 and is_composite(n)}