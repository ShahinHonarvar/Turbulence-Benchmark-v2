def all_pos_ints_exclusive(numbers):
    if len(numbers) < 200:
        return []
    pos_ints = []
    for i in range(90, 200):
        if numbers[i] > 0:
            pos_ints.append(numbers[i])
    return pos_ints