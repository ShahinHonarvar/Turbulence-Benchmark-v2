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

def composite_nums_between_indices(numbers):
    if len(numbers) < 60:
        return set()
    composite_set = set()
    for i in range(59, min(98, len(numbers))):
        if is_composite(numbers[i]):
            composite_set.add(numbers[i])
    return composite_set