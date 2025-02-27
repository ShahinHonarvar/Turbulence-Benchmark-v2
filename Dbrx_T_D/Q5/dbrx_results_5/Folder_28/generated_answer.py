def all_neg_ints_inclusive(numbers):
    if len(numbers) < 64:
        return []
    negatives = []
    for i in range(62, 64):
        if numbers[i] < 0:
            negatives.append(numbers[i])
    return negatives