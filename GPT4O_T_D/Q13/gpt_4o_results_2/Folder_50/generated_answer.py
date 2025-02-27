def find_second_largest_num(numbers):
    if len(numbers) < 85:
        return None
    segment = numbers[70:85]
    if len(segment) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in segment:
        if number > first:
            first, second = (number, first)
        elif number > second:
            second = number
    if second == float('-inf'):
        return None
    return second