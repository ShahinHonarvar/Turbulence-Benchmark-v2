def is_composite(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    if not 1 <= 5 < len(lst):
        return set()
    res = set()
    for i in range(1, 6):
        if is_composite(lst[i]):
            res.add(lst[i])
    return res