def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 5:
        return None
    min_num, second_min_num = (None, None)
    for num in numbers[:5]:
        if min_num is None or num < min_num:
            min_num, second_min_num = (num, min_num)
        elif second_min_num is None or num < second_min_num:
            second_min_num = num
    for num in numbers[5:]:
        if num < min_num:
            min_num, second_min_num = (num, min_num)
        elif min_num < num < second_min_num:
            second_min_num = num
    return second_min_num