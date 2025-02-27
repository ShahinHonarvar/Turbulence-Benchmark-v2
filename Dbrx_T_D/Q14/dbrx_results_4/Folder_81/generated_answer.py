def find_second_smallest_num(numbers):
    numbers_in_range = numbers[10:101]
    if len(numbers_in_range) < 2:
        return None
    min_num, second_min_num = (min(numbers_in_range), max(numbers_in_range))
    for num in numbers_in_range:
        if num < min_num:
            min_num, second_min_num = (num, min_num)
        elif num < second_min_num and num != min_num:
            second_min_num = num
    return second_min_num