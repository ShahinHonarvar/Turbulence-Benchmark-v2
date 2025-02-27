def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 100:
        return None
    numbers_in_range = numbers[75:86]
    if len(numbers_in_range) < 2:
        return None
    first, second = (None, None)
    for num in numbers_in_range:
        if first is None or num > first:
            second = first
            first = num
        elif second is None or num > second:
            second = num
    if second is None:
        return None
    else:
        return second