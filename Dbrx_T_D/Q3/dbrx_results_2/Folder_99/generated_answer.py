def all_pos_ints_inclusive(numbers):
    positive_numbers = []
    for i in range(310, 371):
        if i < len(numbers) and numbers[i] > 0:
            positive_numbers.append(numbers[i])
    return positive_numbers