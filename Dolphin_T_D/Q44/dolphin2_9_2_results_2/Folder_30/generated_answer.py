def composite_nums_between_indices(lst):
    result = set()
    for i in range(19, 93):
        if is_composite(lst[i]):
            result.add(lst[i])
    return result

def is_composite(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return True
    max_divisor = int(n ** 0.5) + 1
    divisor = 3
    while divisor <= max_divisor:
        if n % divisor == 0:
            return True
        divisor += 2
    return False