def all_neg_ints_inclusive(numbers):
    if len(numbers) < 55:
        return []
    neg_ints = []
    for i in range(34, 56):
        if numbers[i] < 0:
            neg_ints.append(numbers[i])
    return neg_ints