def all_pos_ints_inclusive(numbers):
    result = []
    for i in range(8, 10):
        if i < len(numbers) and numbers[i] > 0:
            result.append(numbers[i])
    return result