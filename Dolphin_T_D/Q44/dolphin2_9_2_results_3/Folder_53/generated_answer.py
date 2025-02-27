def is_composite(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for num in range(2, int(n ** 0.5) + 1):
            if n % num == 0:
                return True
        return False

def composite_nums_between_indices(lst):
    return {x for x in lst[222:223] if is_composite(x)}