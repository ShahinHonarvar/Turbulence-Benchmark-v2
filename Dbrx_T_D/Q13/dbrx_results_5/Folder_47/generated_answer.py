def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = max_num = numbers[37]
    second_max_num = None
    for i in range(37, 77):
        if numbers[i] > max_num:
            second_max_num = max_num
            max_num = numbers[i]
        elif second_max_num is None or numbers[i] > second_max_num:
            second_max_num = numbers[i]
    return second_max_num if second_max_num != max_num else None