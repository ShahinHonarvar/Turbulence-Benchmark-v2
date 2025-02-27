def all_even_ints_inclusive(numbers):
    if len(numbers) < 60:
        return []
    result = []
    for i in range(25, 60):
        if numbers[i] % 2 == 0:
            result.append(numbers[i])
    return result