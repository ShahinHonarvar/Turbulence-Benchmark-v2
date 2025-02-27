def all_pos_ints_exclusive(numbers):
    start_index = 13
    end_index = 66
    pos_ints = []
    for i in range(start_index, end_index):
        if numbers[i] > 0:
            pos_ints.append(numbers[i])
    return pos_ints