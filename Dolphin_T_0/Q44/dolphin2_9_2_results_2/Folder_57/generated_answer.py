def composite_nums_between_indices(lst):
    result = set()
    for i in range(25, 60):
        if is_composite(lst[i]):
            result.add(lst[i])
    return result

def is_composite(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False