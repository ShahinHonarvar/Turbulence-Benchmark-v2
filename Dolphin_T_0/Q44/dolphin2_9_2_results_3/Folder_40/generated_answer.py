def is_composite(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    return set((x for i, x in enumerate(lst, 1) if 2 <= i <= len(lst) - 2 and is_composite(x)))