def all_pos_ints_inclusive(numbers):
    if len(numbers) < 58:
        return []
    result = []
    for index in range(56, 58):
        if numbers[index] > 0:
            result.append(numbers[index])
    return result