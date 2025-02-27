def all_even_ints_exclusive(numbers):
    result = []
    for i in range(1, len(numbers) - 1):
        if numbers[i] % 2 == 0:
            result.append(numbers[i])
    return result