def is_composite(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return True
    i = 3
    while i * i <= n:
        if n % i == 0:
            return True
        i += 2
    return False

def composite_nums_between_indices(lst):
    return set((num for num in lst[14:65] if is_composite(num)))