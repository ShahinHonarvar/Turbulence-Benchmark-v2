def all_pos_ints_inclusive(numbers):
    pos_ints = []
    for i in range(max(0, 75), min(len(numbers), 86)):
        if numbers[i] > 0:
            pos_ints.append(numbers[i])
    return pos_ints