def all_pos_ints_inclusive(numbers):
    if len(numbers) < 200:
        return []
    result = []
    for i in range(40, 201):
        if numbers[i] > 0:
            result.append(numbers[i])
    return result