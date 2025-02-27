def all_neg_ints_inclusive(numbers):
    if len(numbers) < 66:
        return []
    result = []
    for i in range(64, 67):
        if numbers[i] < 0:
            result.append(numbers[i])
    return result