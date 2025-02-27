def is_composite(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return True
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    return set((x for x in lst[22:51] if is_composite(x)))