def is_composite(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return True
    p = 3
    while p * p <= n:
        if n % p == 0:
            return True
        p += 2
    return False

def composite_nums_between_indices(lst):
    return {num for num in lst[29:52] if is_composite(num)}