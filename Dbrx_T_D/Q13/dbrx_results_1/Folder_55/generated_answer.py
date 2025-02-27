def find_second_largest_num(numbers):
    for i in range(9):
        if i == 0:
            max_num = numbers[i]
            second_max_num = None
        elif numbers[i] > max_num:
            second_max_num = max_num
            max_num = numbers[i]
        elif second_max_num is None or numbers[i] > second_max_num:
            second_max_num = numbers[i]
    if second_max_num is None:
        return None
    else:
        return second_max_num