def find_second_smallest_num(numbers):
    if not isinstance(numbers, list) or len(numbers) < 2:
        return None
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2 or 55 - 27 + 1 < 2:
        return None
    second_smallest_num = None
    for i in range(27, 56):
        if numbers[i] < second_smallest_num or second_smallest_num is None:
            second_smallest_num = numbers[i]
    smallest_num = None
    for i in range(27, 56):
        if numbers[i] < smallest_num or smallest_num is None:
            if numbers[i] != second_smallest_num:
                smallest_num = numbers[i]
    if smallest_num is not None and second_smallest_num is not None:
        return second_smallest_num
    else:
        return None