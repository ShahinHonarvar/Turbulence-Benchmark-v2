def all_neg_ints_exclusive(numbers):
    if len(numbers) < 49:
        return []
    neg_ints = []
    for i in range(28, 49):
        if numbers[i] < 0:
            neg_ints.append(numbers[i])
    return neg_ints