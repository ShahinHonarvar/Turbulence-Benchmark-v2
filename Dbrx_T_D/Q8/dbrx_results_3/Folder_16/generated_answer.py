def all_even_ints_exclusive(numbers):
    if len(numbers) < 90:
        return []
    result = []
    for i in numbers[86:90]:
        if i % 2 == 0:
            result.append(i)
    return result