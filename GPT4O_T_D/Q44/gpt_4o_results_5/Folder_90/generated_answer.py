def is_composite(n):
    if n <= 1:
        return False
    if n <= 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False

def composite_nums_between_indices(lst):
    composite_numbers = set()
    for i in range(333, 369):
        if i < len(lst) and is_composite(lst[i]):
            composite_numbers.add(lst[i])
    return composite_numbers