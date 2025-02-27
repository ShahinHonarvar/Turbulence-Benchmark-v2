def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (None, None)
    for num in numbers:
        if first is None or num > first:
            second = first
            first = num
        elif second is None or num > second:
            second = num
    return second if second is not None else None