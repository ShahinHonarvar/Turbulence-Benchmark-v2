def all_odd_ints_exclusive(numbers):
    if len(numbers) < 200:
        return []
    result = []
    for i in range(60, 200):
        if numbers[i] % 2 != 0:
            result.append(numbers[i])
    return result