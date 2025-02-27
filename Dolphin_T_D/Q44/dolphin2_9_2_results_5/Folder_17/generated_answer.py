def composite_nums_between_indices(lst):
    composites = set()
    for i in range(50, 55):
        if not is_prime(lst[i]):
            composites.add(lst[i])
    return composites

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True