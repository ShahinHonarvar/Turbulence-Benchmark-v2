def find_second_largest_num(numbers):
    if len(numbers) < 60:
        return None
    sublist = numbers[25:60]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in sublist:
        if number > first:
            first, second = (number, first)
        elif number > second:
            second = number
    return second if second != float('-inf') else None