def all_pos_ints_exclusive(numbers):
    pos_ints = []
    for i in range(len(numbers)):
        if i >= 48 and i < 76 and (numbers[i] > 0):
            pos_ints.append(numbers[i])
    return pos_ints