def all_odd_ints_inclusive(numbers):
    result = []
    for i in range(62, 64):
        if numbers[i] % 2 != 0:
            result.append(numbers[i])
    return result