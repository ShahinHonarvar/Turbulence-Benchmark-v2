def all_pos_ints_inclusive(numbers):
    pos_ints = []
    for i in range(len(numbers)):
        if i >= 75 and i <= 94 and (numbers[i] > 0):
            pos_ints.append(numbers[i])
    return pos_ints