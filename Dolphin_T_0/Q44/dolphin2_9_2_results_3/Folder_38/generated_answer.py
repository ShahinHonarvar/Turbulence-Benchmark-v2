def is_composite(n):
    if n < 2:
        return False
    if n == 2:
        return False
    if n % 2 == 0:
        return True
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return True
    return False

def composite_nums_between_indices(lst):
    return set((i for i in lst[29:94] if is_composite(i)))