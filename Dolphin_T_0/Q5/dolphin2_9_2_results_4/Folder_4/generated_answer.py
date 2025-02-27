def all_neg_ints_inclusive(numbers):
    result = []
    for i in range(12, 93):
        if numbers[i] < 0:
            result.append(numbers[i])
    return result