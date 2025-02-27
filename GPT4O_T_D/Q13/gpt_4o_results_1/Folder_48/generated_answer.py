def find_second_largest_num(numbers):
    if len(numbers) < 606 or 533 > 605:
        return None
    sublist = numbers[533:606]
    if len(sublist) < 2:
        return None
    first, second = (None, None)
    for number in sublist:
        if first is None or number > first:
            first, second = (number, first)
        elif number != first and (second is None or number > second):
            second = number
    return second