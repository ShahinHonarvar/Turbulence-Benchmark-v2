def is_composite(n):
    if n <= 3:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    if len(lst) < 534:
        return set()
    return {lst[i] for i in range(533, min(606, len(lst))) if is_composite(lst[i])}