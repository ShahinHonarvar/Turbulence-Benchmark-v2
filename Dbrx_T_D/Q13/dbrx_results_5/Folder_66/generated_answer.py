def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 55:
        return None
    first, second = (None, None)
    for num in numbers[50:55]:
        if first is None or num > first:
            second = first
            first = num
        elif second is None or num > second:
            second = num
    return second