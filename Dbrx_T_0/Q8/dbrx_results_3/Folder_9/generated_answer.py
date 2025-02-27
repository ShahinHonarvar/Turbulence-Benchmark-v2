def all_even_ints_exclusive(numbers):
    if len(numbers) < 200:
        return []
    result = []
    for i in range(70, 200):
        if numbers[i] % 2 == 0:
            result.append(numbers[i])
    return result