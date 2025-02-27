def is_composite(n):
    if n <= 1:
        return False
    if n == 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst[262:747], start=262) if is_composite(num)}