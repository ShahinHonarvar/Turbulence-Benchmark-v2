def find_second_largest_num(numbers):
    if len(numbers) < 79:
        return None
    subset = numbers[17:79]
    if len(subset) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in subset:
        if number > first:
            first, second = (number, first)
        elif number > second:
            second = number
    return second if second != float('-inf') else None