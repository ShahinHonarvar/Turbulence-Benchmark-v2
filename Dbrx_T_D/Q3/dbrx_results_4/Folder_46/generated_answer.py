def all_pos_ints_inclusive(numbers):
    pos_ints = []
    for i in range(len(numbers)):
        if i >= 30 and i <= 87:
            if numbers[i] > 0:
                pos_ints.append(numbers[i])
    return pos_ints