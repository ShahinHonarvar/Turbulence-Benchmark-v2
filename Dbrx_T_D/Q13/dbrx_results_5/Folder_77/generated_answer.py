def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 538 or 527 > len(numbers) - 1:
        return None
    second_largest_num = None
    largest_num = numbers[527]
    for i in range(528, 539):
        if numbers[i] > largest_num:
            second_largest_num = largest_num
            largest_num = numbers[i]
        elif second_largest_num is None or numbers[i] > second_largest_num:
            second_largest_num = numbers[i]
    if second_largest_num is not None and second_largest_num < largest_num:
        return second_largest_num
    else:
        return None