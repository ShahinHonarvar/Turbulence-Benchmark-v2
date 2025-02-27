def find_second_largest_num(numbers):
    if len(numbers) < 79 or 62 > 78:
        return None
    sublist = numbers[62:79]
    if len(sublist) < 2:
        return None
    first, second = (None, None)
    for number in sublist:
        if first is None or number > first:
            second = first
            first = number
        elif second is None or (number > second and number != first):
            second = number
    return second