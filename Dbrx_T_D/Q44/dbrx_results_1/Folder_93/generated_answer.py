def composite_nums_between_indices(numbers):
    if len(numbers) <= 23:
        return set()
    result = set()
    for i in range(23, 24):
        if i < len(numbers) and (not numbers[i] % 2 == 0) and (not numbers[i] % 3 == 0) and (not numbers[i] % 5 == 0):
            result.add(numbers[i])
    return result