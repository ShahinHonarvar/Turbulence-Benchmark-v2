def all_pos_ints_inclusive(numbers):
    if len(numbers) == 0:
        return []
    pos_ints = []
    for i in range(min(0, numbers[0]), max(len(numbers), numbers[0]) + 1):
        if numbers[i] > 0:
            pos_ints.append(numbers[i])
    return pos_ints