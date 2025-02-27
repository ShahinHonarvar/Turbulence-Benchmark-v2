def all_even_ints_inclusive(numbers):
    if len(numbers) < 40:
        return []
    result = []
    for i in range(28, 41):
        if numbers[i] % 2 == 0:
            result.append(numbers[i])
    return result