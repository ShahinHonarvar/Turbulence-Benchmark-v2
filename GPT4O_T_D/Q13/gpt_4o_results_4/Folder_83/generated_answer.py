def find_second_largest_num(numbers):
    if len(numbers) < 91:
        return None
    subrange = numbers[90:91]
    if len(subrange) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in subrange:
        if number > first:
            first, second = (number, first)
        elif number > second and number != first:
            second = number
    return second if second != float('-inf') else None