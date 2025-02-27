def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (None, None)
    for num in numbers[12:93]:
        if first is None or num >= first:
            second = first
            first = num
        elif second is None or num > second:
            second = num
    if second is None:
        return None
    return second