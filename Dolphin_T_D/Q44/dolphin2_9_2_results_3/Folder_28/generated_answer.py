def is_composite(n):
    if n <= 1:
        return False
    if n == 2:
        return False
    if n % 2 == 0:
        return True
    sqr = int(n ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    return {num for num in lst[22:89] if is_composite(num)}