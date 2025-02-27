def all_neg_ints_inclusive(numbers):
    result = []
    for i in range(min(len(numbers), 5)):
        if numbers[i] < 0:
            result.append(numbers[i])
    return result