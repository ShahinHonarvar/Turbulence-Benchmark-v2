def is_composite(n):
    if n < 4:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(533, min(606, len(numbers))):
        if is_composite(numbers[i]):
            composites.add(numbers[i])
    return composites