def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num_1, min_num_2 = (None, None)
    for i in range(29, 80):
        if min_num_1 is None or numbers[i] < min_num_1:
            min_num_2 = min_num_1
            min_num_1 = numbers[i]
        elif min_num_2 is None or numbers[i] < min_num_2:
            min_num_2 = numbers[i]
    if min_num_2 is None or min_num_2 == min_num_1:
        return None
    else:
        return min_num_2