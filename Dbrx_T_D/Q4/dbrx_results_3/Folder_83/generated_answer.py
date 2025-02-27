def all_pos_ints_exclusive(numbers):
    if len(numbers) < 200:
        return []
    result = []
    for i in range(90, 200):
        if numbers[i] > 0:
            result.append(numbers[i])
    return result