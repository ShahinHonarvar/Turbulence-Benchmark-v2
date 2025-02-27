def all_pos_ints_inclusive(numbers):
    pos_ints = []
    for i in range(min(0, len(numbers)), min(len(numbers), 0) + 1):
        if numbers[i] > 0:
            pos_ints.append(numbers[i])
    return pos_ints