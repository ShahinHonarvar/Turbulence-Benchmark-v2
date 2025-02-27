def find_second_smallest_num(numbers):
    if len(numbers) < 51 or len(numbers) > 100:
        return None
    min_num, second_min_num = (None, None)
    for num in numbers[22:51]:
        if min_num is None or num < min_num:
            second_min_num = min_num
            min_num = num
        elif second_min_num is None or num < second_min_num:
            second_min_num = num
    return second_min_num