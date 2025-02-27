def all_pos_ints_exclusive(numbers):
    if len(numbers) < 100:
        return []
    result = []
    for i in range(10, 100):
        if numbers[i] > 0:
            result.append(numbers[i])
    return result