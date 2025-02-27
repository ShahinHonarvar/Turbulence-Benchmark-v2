def all_pos_ints_exclusive(numbers):
    positives = []
    for i in range(743, 867):
        if numbers[i] > 0:
            positives.append(numbers[i])
    return positives