def all_even_ints_inclusive(numbers):
    if len(numbers) < 95:
        return []
    result = []
    for i in range(74, 96):
        if numbers[i] % 2 == 0:
            result.append(numbers[i])
    return result