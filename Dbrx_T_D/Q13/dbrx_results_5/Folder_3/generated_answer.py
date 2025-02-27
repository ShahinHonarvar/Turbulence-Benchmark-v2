def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first_largest_ind, second_largest_ind = (None, None)
    for i in range(62, 93):
        if first_largest_ind is None or numbers[i] > numbers[first_largest_ind]:
            second_largest_ind = first_largest_ind
            first_largest_ind = i
        elif second_largest_ind is None or numbers[i] > numbers[second_largest_ind]:
            second_largest_ind = i
    return None if second_largest_ind is None else numbers[second_largest_ind]