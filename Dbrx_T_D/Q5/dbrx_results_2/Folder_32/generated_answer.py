def all_neg_ints_inclusive(numbers):
    if len(numbers) < 97:
        return []
    result = []
    for i in range(21, 98):
        if numbers[i] < 0:
            result.append(numbers[i])
    return result