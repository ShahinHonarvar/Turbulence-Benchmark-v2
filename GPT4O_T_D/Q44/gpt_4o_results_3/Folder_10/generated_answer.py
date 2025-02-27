def is_composite(n):
    if n <= 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False

def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst[37:52]) if is_composite(x)}