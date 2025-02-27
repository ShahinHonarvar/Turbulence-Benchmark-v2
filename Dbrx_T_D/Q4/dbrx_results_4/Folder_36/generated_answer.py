def all_pos_ints_exclusive(numbers):
    start_index = 598
    end_index = 767
    pos_ints = []
    for i in range(len(numbers)):
        if i >= start_index and i < end_index and (numbers[i] > 0):
            pos_ints.append(numbers[i])
    return pos_ints