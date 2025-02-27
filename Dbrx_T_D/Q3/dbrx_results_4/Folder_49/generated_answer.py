def all_pos_ints_inclusive(numbers):
    if len(numbers) < 200:
        return []
    positive_integers = []
    for i in range(80, 201):
        if numbers[i] > 0:
            positive_integers.append(numbers[i])
    return positive_integers