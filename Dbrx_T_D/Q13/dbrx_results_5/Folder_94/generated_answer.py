def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num, second_num = (None, None)
    for i in range(28, 41):
        num = numbers[i]
        if min_num is None or num > min_num:
            second_num = min_num
            min_num = num
        elif second_num is None or num > second_num:
            second_num = num
    return second_num