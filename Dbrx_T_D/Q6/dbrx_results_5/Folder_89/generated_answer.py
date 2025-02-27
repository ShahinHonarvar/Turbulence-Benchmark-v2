def all_neg_ints_exclusive(numbers):
    result = []
    for i in range(len(numbers)):
        if i >= 51 and i < 76 and (numbers[i] < 0):
            result.append(numbers[i])
    return result