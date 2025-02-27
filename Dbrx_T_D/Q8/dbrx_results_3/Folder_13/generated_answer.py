def all_even_ints_exclusive(numbers):
    if len(numbers) < 84:
        return []
    result = []
    for i in numbers[73:84]:
        if i % 2 == 0:
            result.append(i)
    return result