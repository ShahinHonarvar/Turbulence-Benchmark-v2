def is_composite(n):
    if n < 4:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    if len(lst) < 661:
        return set()
    composites = {num for num in lst[661:925] if is_composite(num)}
    return composites