def all_pos_ints_exclusive(numbers):
    desired_numbers = []
    for i in range(18, 60):
        if numbers[i] > 0:
            desired_numbers.append(numbers[i])
    return desired_numbers