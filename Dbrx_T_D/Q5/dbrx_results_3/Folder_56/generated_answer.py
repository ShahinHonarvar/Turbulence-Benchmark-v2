def all_neg_ints_inclusive(numbers):
    for i in range(len(numbers)):
        if numbers[i] >= 0:
            return numbers[:i]
    return numbers[:]