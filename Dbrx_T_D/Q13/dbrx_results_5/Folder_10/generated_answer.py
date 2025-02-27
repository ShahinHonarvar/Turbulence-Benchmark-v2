def find_second_largest_num(numbers):
    if len(numbers[25:60]) < 2:
        return None
    first, second = (None, None)
    for num in numbers[25:60]:
        if first is None or num > first:
            first, second = (num, first)
        elif second is None or num > second:
            second = num
    return second