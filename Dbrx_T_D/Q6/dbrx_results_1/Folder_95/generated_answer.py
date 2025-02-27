def all_neg_ints_exclusive(numbers):
    if len(numbers) < 80:
        return []
    result = []
    for i in range(25, 80):
        if numbers[i] < 0:
            result.append(numbers[i])
    return result