def is_composite(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    result = set()
    for i in range(19, 93):
        if is_composite(lst[i]):
            result.add(lst[i])
    return result