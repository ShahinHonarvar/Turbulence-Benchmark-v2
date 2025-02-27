def find_second_largest_num(numbers):
    sublist = numbers[37:52]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in sublist:
        if number > first:
            first, second = (number, first)
        elif first > number > second:
            second = number
    if second == float('-inf'):
        return None
    return second