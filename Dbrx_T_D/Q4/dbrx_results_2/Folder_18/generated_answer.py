def all_pos_ints_exclusive(numbers):
    if len(numbers) < 84:
        return []
    result = []
    for i in range(57, 84):
        if numbers[i] > 0:
            result.append(numbers[i])
    return result