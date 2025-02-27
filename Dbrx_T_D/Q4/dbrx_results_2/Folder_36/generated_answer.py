def all_pos_ints_exclusive(numbers):
    pos_numbers = []
    for i in range(len(numbers)):
        if i >= 598 and i < 767:
            if numbers[i] > 0:
                pos_numbers.append(numbers[i])
    return pos_numbers