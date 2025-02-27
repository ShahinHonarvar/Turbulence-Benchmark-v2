def all_pos_ints_inclusive(numbers):
    if len(numbers) < 201:
        return []
    result = []
    for i in range(20, 201):
        if numbers[i] > 0:
            result.append(numbers[i])
    return result