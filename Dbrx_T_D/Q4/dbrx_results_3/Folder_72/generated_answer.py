def all_pos_ints_exclusive(numbers):
    if len(numbers) < 89:
        return []
    result = []
    for i in range(56, 88):
        if numbers[i] > 0:
            result.append(numbers[i])
    return result