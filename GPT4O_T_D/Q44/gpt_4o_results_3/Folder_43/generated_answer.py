def is_composite(n):
    if n < 4:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(numbers):
    if len(numbers) < 32:
        return set()
    result = set()
    for i in range(31, min(73, len(numbers))):
        if is_composite(numbers[i]):
            result.add(numbers[i])
    return result