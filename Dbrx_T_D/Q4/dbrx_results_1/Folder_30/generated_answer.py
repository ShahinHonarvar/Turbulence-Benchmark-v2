def all_pos_ints_exclusive(numbers):
    start_index = 86
    end_index = 89
    if len(numbers) < end_index:
        return []
    positive_integers = []
    for i in range(start_index, end_index):
        if numbers[i] > 0:
            positive_integers.append(numbers[i])
    return positive_integers