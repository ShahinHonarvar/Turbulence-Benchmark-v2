def is_composite(n):
    if n <= 1:
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
    return set((x for i, x in enumerate(lst) if i in range(34, 56) and is_composite(x)))