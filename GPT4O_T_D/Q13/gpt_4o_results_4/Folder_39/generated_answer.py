def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    sublist = numbers[20:31]
    if len(sublist) < 2:
        return None
    first, second = (None, None)
    for number in sublist:
        if first is None or number > first:
            first, second = (number, first)
        elif second is None or number > second:
            second = number
    return second