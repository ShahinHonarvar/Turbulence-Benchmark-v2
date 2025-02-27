def all_pos_ints_inclusive(numbers):
    if len(numbers) < 370:
        return []
    result = []
    for i in range(310, 371):
        if numbers[i] > 0:
            result.append(numbers[i])
    return result