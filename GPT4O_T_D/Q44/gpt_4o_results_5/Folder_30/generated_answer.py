def is_composite(n):
    if n <= 3:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    if len(lst) < 20:
        return set()
    return {num for num in lst[19:93] if is_composite(num)}