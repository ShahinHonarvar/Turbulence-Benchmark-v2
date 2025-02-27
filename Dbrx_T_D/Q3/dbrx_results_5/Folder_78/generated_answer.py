def all_pos_ints_inclusive(numbers):
    if len(numbers) < 51:
        return []
    pos_ints = []
    for i in range(43, 52):
        if numbers[i] > 0:
            pos_ints.append(numbers[i])
    return pos_ints