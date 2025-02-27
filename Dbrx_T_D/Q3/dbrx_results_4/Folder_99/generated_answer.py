def all_pos_ints_inclusive(numbers):
    if len(numbers) < 370:
        return []
    pos_ints = []
    for i in range(310, 371):
        if numbers[i] > 0:
            pos_ints.append(numbers[i])
    return pos_ints