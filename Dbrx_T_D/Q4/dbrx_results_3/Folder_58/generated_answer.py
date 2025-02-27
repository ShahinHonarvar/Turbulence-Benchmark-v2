def all_pos_ints_exclusive(numbers):
    start = 276
    end = 376
    result = []
    for i in range(start, end):
        if i < len(numbers) and numbers[i] > 0:
            result.append(numbers[i])
    return result